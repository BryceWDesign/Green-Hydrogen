"""Safety preflight gates for Green-Hydrogen validation runs.

This module is deliberately conservative. It does not operate hardware and it
cannot prove hydrogen production. It only checks whether a requested run has a
complete, explicitly passing safety preflight record before any run or claim
review is allowed to continue.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from .policy import check_branch_policy, normalize_branch


REQUIRED_TRUE_FIELDS = (
    "operator_present",
    "ventilation_present",
    "no_pressure_storage",
    "no_sealed_accumulation",
    "no_ignition_sources",
    "emergency_disconnect_present",
    "leak_check_passed",
    "water_electric_separation_confirmed",
    "sensors_connected",
    "sensor_wetness_protection_confirmed",
    "gas_path_documented",
    "vent_path_defined",
    "run_duration_bounded",
    "prior_anomalies_resolved",
    "evidence_forms_ready",
)

SUPPORTED_PREFLIGHT_BRANCHES = (
    "baseline",
    "gankyil_a",
    "solar_electrical",
    "solar_thermal_assist",
    "plasma_catalyst",
    "pec",
    "redox",
    "hybrid_future",
)


@dataclass(frozen=True)
class SafetyPreflightResult:
    """Result of a safety preflight check."""

    passed: bool
    status: str
    branch: str
    failed_fields: tuple[str, ...] = field(default_factory=tuple)
    reasons: tuple[str, ...] = field(default_factory=tuple)
    required_next: tuple[str, ...] = field(default_factory=tuple)

    def to_record(self) -> dict[str, Any]:
        """Return a serializable preflight result."""
        return {
            "passed": self.passed,
            "status": self.status,
            "branch": self.branch,
            "failed_fields": list(self.failed_fields),
            "reasons": list(self.reasons),
            "required_next": list(self.required_next),
        }


def passing_dry_baseline_preflight() -> dict[str, Any]:
    """Return a complete dry baseline preflight record for software tests.

    This is a dry documentation fixture only. It is not a physical safety
    certification and must not be treated as permission to operate hardware.
    """
    return {
        "operator_present": True,
        "ventilation_present": True,
        "no_pressure_storage": True,
        "no_sealed_accumulation": True,
        "no_ignition_sources": True,
        "emergency_disconnect_present": True,
        "leak_check_passed": True,
        "water_electric_separation_confirmed": True,
        "sensors_connected": True,
        "sensor_wetness_protection_confirmed": True,
        "gas_path_documented": True,
        "vent_path_defined": True,
        "branch_selected": "baseline",
        "run_duration_bounded": True,
        "prior_anomalies_resolved": True,
        "evidence_forms_ready": True,
        "sensor_wetness_observed": False,
        "pressure_storage_present": False,
        "flame_test_present": False,
        "advanced_branch_requested": False,
        "preflight_scope": "dry_software_fixture_only",
    }


def _failed_required_true_fields(preflight: Mapping[str, Any]) -> tuple[str, ...]:
    """Return required boolean fields that are not explicitly true."""
    return tuple(field for field in REQUIRED_TRUE_FIELDS if preflight.get(field) is not True)


def _known_text(value: Any) -> bool:
    """Return True when a value is meaningful enough for gatekeeping."""
    if value is None:
        return False

    if isinstance(value, str):
        return value.strip().lower() not in {
            "",
            "unknown",
            "not_measured",
            "not_applicable",
            "n/a",
            "na",
        }

    return True


def _branch_from_preflight(preflight: Mapping[str, Any]) -> str:
    """Resolve the branch selected in the preflight record."""
    return normalize_branch(preflight.get("branch_selected"))


def _branch_from_intent(run_intent: Mapping[str, Any]) -> str:
    """Resolve the branch requested by the run intent."""
    return normalize_branch(run_intent.get("branch"))


def run_safety_preflight(
    run_intent: Mapping[str, Any], preflight: Mapping[str, Any]
) -> SafetyPreflightResult:
    """Check policy and safety preflight records for a requested run.

    A pass requires:
    - branch policy allows the run intent,
    - every required safety field is explicitly true,
    - the preflight branch matches the run-intent branch,
    - no hard-denial condition is present.

    The function fails closed: malformed records, unknown branches, missing
    booleans, pressure storage, flame tests, sensor wetness, or unresolved
    anomalies block the run.
    """
    if not isinstance(run_intent, Mapping):
        return SafetyPreflightResult(
            passed=False,
            status="blocked_by_policy",
            branch="unknown",
            failed_fields=("run_intent",),
            reasons=("run_intent is not a mapping",),
            required_next=("provide a structured run intent record",),
        )

    if not isinstance(preflight, Mapping):
        branch = _branch_from_intent(run_intent)
        return SafetyPreflightResult(
            passed=False,
            status="blocked_by_safety_gate",
            branch=branch,
            failed_fields=("safety_preflight",),
            reasons=("safety preflight is not a mapping",),
            required_next=("provide a structured safety preflight record",),
        )

    policy_decision = check_branch_policy(run_intent)
    if not policy_decision.allowed:
        return SafetyPreflightResult(
            passed=False,
            status=policy_decision.status,
            branch=policy_decision.branch,
            failed_fields=("run_intent",),
            reasons=policy_decision.reasons,
            required_next=policy_decision.required_next,
        )

    intent_branch = _branch_from_intent(run_intent)
    preflight_branch = _branch_from_preflight(preflight)
    failed_fields = list(_failed_required_true_fields(preflight))
    reasons: list[str] = []
    required_next: list[str] = []

    if not _known_text(run_intent.get("run_id")):
        failed_fields.append("run_id")
        reasons.append("run_id is missing")
        required_next.append("create a stable run_id before preflight")

    if "branch_selected" not in preflight or not _known_text(preflight.get("branch_selected")):
        failed_fields.append("branch_selected")
        reasons.append("branch_selected is missing")
        required_next.append("select the run branch before preflight")
    elif preflight_branch not in SUPPORTED_PREFLIGHT_BRANCHES:
        failed_fields.append("branch_selected")
        reasons.append(f"branch_selected '{preflight_branch}' is not supported")
        required_next.append("select a supported branch before preflight")
    elif preflight_branch != intent_branch:
        failed_fields.append("branch_selected")
        reasons.append(
            f"preflight branch '{preflight_branch}' does not match intent branch '{intent_branch}'"
        )
        required_next.append("make run intent and preflight branch selection match")

    if preflight.get("pressure_storage_present") is True:
        failed_fields.append("pressure_storage_present")
        reasons.append("pressure storage is present")
        required_next.append("remove pressure storage from GH-BENCH-A0")

    if run_intent.get("pressure_storage_requested") is True:
        failed_fields.append("pressure_storage_requested")
        reasons.append("pressure storage was requested")
        required_next.append("remove pressure storage from the run intent")

    if preflight.get("flame_test_present") is True:
        failed_fields.append("flame_test_present")
        reasons.append("flame testing is present")
        required_next.append("remove flame testing and use hydrogen-specific detection")

    if run_intent.get("flame_test_requested") is True:
        failed_fields.append("flame_test_requested")
        reasons.append("flame testing was requested")
        required_next.append("remove flame testing from the run intent")

    if preflight.get("sensor_wetness_observed") is True:
        failed_fields.append("sensor_wetness_observed")
        reasons.append("sensor wetness was observed")
        required_next.append("protect the sensor path and rerun preflight")

    if preflight.get("advanced_branch_requested") is True and intent_branch == "baseline":
        failed_fields.append("advanced_branch_requested")
        reasons.append("advanced branch was requested inside a baseline preflight")
        required_next.append("keep advanced branch evidence separate from baseline runs")

    for field in REQUIRED_TRUE_FIELDS:
        if preflight.get(field) is not True:
            reasons.append(f"{field} is not explicitly true")
            required_next.append(f"confirm {field} before run")

    if failed_fields:
        unique_failed = tuple(dict.fromkeys(failed_fields))
        unique_reasons = tuple(dict.fromkeys(reasons))
        unique_required_next = tuple(dict.fromkeys(required_next))

        return SafetyPreflightResult(
            passed=False,
            status="blocked_by_safety_gate",
            branch=intent_branch,
            failed_fields=unique_failed,
            reasons=unique_reasons,
            required_next=unique_required_next,
        )

    return SafetyPreflightResult(
        passed=True,
        status="pass",
        branch=intent_branch,
        failed_fields=(),
        reasons=("all required safety preflight fields passed",),
        required_next=("preserve preflight record with the evidence bundle",),
    )
