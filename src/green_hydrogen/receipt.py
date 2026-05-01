"""Receipt generation for Green-Hydrogen validation runs.

Receipts are compact summaries of run evidence. A receipt does not replace raw
evidence. It records what exists, what is missing, and what claim status is
currently allowed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


BASELINE_REQUIRED_RECORDS = (
    "run_intent",
    "safety_preflight",
    "water_record",
    "power_record",
    "gas_record",
    "carbon_record",
    "notes",
)

OPTIONAL_RECORDS = (
    "thermal_record",
    "branch_review",
    "calibration_record",
    "phase_management_metrics",
    "sensor_log",
    "setup_photos",
)


@dataclass(frozen=True)
class Receipt:
    """Reviewer-facing run receipt."""

    run_id: str
    branch: str
    objective: str
    preflight_status: str
    run_started: bool
    run_completed: bool
    records_present: tuple[str, ...] = field(default_factory=tuple)
    missing_records: tuple[str, ...] = field(default_factory=tuple)
    hydrogen_specific_detection_present: bool = False
    green_claim_requested: bool = False
    green_claim_supported: bool = False
    advanced_branch_requested: bool = False
    advanced_branch_approved: bool = False
    anomalies: tuple[str, ...] = field(default_factory=tuple)
    claim_status: str = "no_claim"
    operator_notes: str = ""

    def to_record(self) -> dict[str, Any]:
        """Return a serializable receipt."""
        return {
            "run_id": self.run_id,
            "branch": self.branch,
            "objective": self.objective,
            "preflight_status": self.preflight_status,
            "run_started": self.run_started,
            "run_completed": self.run_completed,
            "records_present": list(self.records_present),
            "missing_records": list(self.missing_records),
            "hydrogen_specific_detection_present": self.hydrogen_specific_detection_present,
            "green_claim_requested": self.green_claim_requested,
            "green_claim_supported": self.green_claim_supported,
            "advanced_branch_requested": self.advanced_branch_requested,
            "advanced_branch_approved": self.advanced_branch_approved,
            "anomalies": list(self.anomalies),
            "claim_status": self.claim_status,
            "operator_notes": self.operator_notes,
        }


def _known(value: Any) -> bool:
    """Return True when a value is meaningfully present."""
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


def _record_present(bundle: Mapping[str, Any], key: str) -> bool:
    """Return True if a named record exists and is not empty."""
    value = bundle.get(key)
    if isinstance(value, Mapping):
        return bool(value)
    return _known(value)


def present_records(bundle: Mapping[str, Any]) -> tuple[str, ...]:
    """Return known record names present in a bundle."""
    known_records: list[str] = []

    for key in BASELINE_REQUIRED_RECORDS + OPTIONAL_RECORDS:
        if _record_present(bundle, key):
            known_records.append(key)

    return tuple(known_records)


def missing_baseline_records(bundle: Mapping[str, Any]) -> tuple[str, ...]:
    """Return required baseline records missing from a bundle."""
    return tuple(key for key in BASELINE_REQUIRED_RECORDS if not _record_present(bundle, key))


def derive_claim_status(bundle: Mapping[str, Any]) -> str:
    """Derive a conservative claim status from bundle flags and records."""
    preflight = bundle.get("safety_preflight", {})
    gas = bundle.get("gas_record", {})
    carbon = bundle.get("carbon_record", {})

    if isinstance(preflight, Mapping) and preflight.get("passed") is False:
        return "blocked_by_safety_gate"

    missing = missing_baseline_records(bundle)
    if missing:
        return "blocked_by_missing_evidence"

    if isinstance(gas, Mapping):
        if gas.get("sensor_wetness_observed") is True:
            return "inconclusive"

        if gas.get("hydrogen_specific_detection_present") is not True:
            return "rejected"

    if bundle.get("advanced_branch_requested") is True and bundle.get(
        "advanced_branch_approved"
    ) is not True:
        return "blocked_by_advanced_branch_policy"

    if bundle.get("branch") == "gankyil_a":
        metrics = bundle.get("phase_management_metrics", {})
        if isinstance(metrics, Mapping) and metrics.get("phase_management_metric_improved") is True:
            return "accepted_bounded_phase_management_improvement"
        return "inconclusive"

    if bundle.get("green_claim_requested") is True:
        if not isinstance(carbon, Mapping):
            return "blocked_by_missing_evidence"

        if carbon.get("green_claim_supported") is True:
            return "accepted_bounded_result"

        return "inconclusive"

    return "accepted_bounded_result"


def create_receipt(bundle: Mapping[str, Any]) -> Receipt:
    """Create a conservative receipt from a run bundle mapping."""
    run_intent = bundle.get("run_intent", {})
    safety_preflight = bundle.get("safety_preflight", {})
    gas_record = bundle.get("gas_record", {})

    if not isinstance(run_intent, Mapping):
        run_intent = {}

    if not isinstance(safety_preflight, Mapping):
        safety_preflight = {}

    if not isinstance(gas_record, Mapping):
        gas_record = {}

    records_present = present_records(bundle)
    missing_records = missing_baseline_records(bundle)

    anomalies_value = bundle.get("anomalies", ())
    if isinstance(anomalies_value, str):
        anomalies = (anomalies_value,)
    elif isinstance(anomalies_value, list | tuple):
        anomalies = tuple(str(item) for item in anomalies_value)
    else:
        anomalies = ()

    return Receipt(
        run_id=str(run_intent.get("run_id") or bundle.get("run_id") or "unknown"),
        branch=str(run_intent.get("branch") or bundle.get("branch") or "unknown"),
        objective=str(run_intent.get("objective") or bundle.get("objective") or "unknown"),
        preflight_status=str(
            safety_preflight.get("status")
            or safety_preflight.get("preflight_status")
            or bundle.get("preflight_status")
            or "unknown"
        ),
        run_started=bool(bundle.get("run_started")),
        run_completed=bool(bundle.get("run_completed")),
        records_present=records_present,
        missing_records=missing_records,
        hydrogen_specific_detection_present=bool(
            gas_record.get("hydrogen_specific_detection_present")
        ),
        green_claim_requested=bool(bundle.get("green_claim_requested")),
        green_claim_supported=bool(bundle.get("green_claim_supported")),
        advanced_branch_requested=bool(bundle.get("advanced_branch_requested")),
        advanced_branch_approved=bool(bundle.get("advanced_branch_approved")),
        anomalies=anomalies,
        claim_status=derive_claim_status(bundle),
        operator_notes=str(bundle.get("operator_notes") or ""),
    )


def receipt_summary_text(receipt: Receipt) -> str:
    """Return a short reviewer-facing text summary."""
    if receipt.claim_status == "accepted_bounded_result":
        return (
            f"Run {receipt.run_id} was accepted as a bounded result. "
            "This does not prove green hydrogen, efficiency, commercial readiness, "
            "or field readiness."
        )

    if receipt.claim_status == "accepted_bounded_phase_management_improvement":
        return (
            f"Run {receipt.run_id} was accepted as a bounded phase-management result. "
            "This does not prove improved hydrogen production or efficiency."
        )

    if receipt.claim_status.startswith("blocked"):
        return (
            f"Run {receipt.run_id} was blocked with status {receipt.claim_status}. "
            "No physical or claim escalation should proceed until the blocking issue is resolved."
        )

    if receipt.claim_status == "rejected":
        return (
            f"Run {receipt.run_id} was rejected. The evidence should be preserved as a failed "
            "or negative-control artifact."
        )

    return (
        f"Run {receipt.run_id} is {receipt.claim_status}. The result requires review before "
        "any stronger claim is made."
    )
