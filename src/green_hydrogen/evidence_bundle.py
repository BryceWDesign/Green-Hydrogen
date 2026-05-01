"""Evidence bundle helpers for Green-Hydrogen.

Evidence bundles are dictionaries or folder-equivalent records describing a run.
This module checks structure only. It does not verify real-world sensor truth.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


BASELINE_REQUIRED_KEYS = (
    "run_intent",
    "safety_preflight",
    "water_record",
    "power_record",
    "gas_record",
    "carbon_record",
    "receipt",
    "acceptance",
    "notes",
)

GANKYIL_REQUIRED_KEYS = (
    "baseline_run_reference",
    "gankyil_run_reference",
    "comparison_conditions",
    "phase_management_metrics",
    "acceptance",
    "notes",
)

ADVANCED_REQUIRED_KEYS = (
    "run_intent",
    "branch_review",
    "safety_preflight",
    "branch_specific_record",
    "gas_record",
    "power_record",
    "acceptance",
    "notes",
)


@dataclass(frozen=True)
class BundleCheck:
    """Result from evidence-bundle completeness check."""

    complete: bool
    status: str
    branch: str
    present: tuple[str, ...] = field(default_factory=tuple)
    missing: tuple[str, ...] = field(default_factory=tuple)
    warnings: tuple[str, ...] = field(default_factory=tuple)

    def to_record(self) -> dict[str, Any]:
        """Return serializable bundle check."""
        return {
            "complete": self.complete,
            "status": self.status,
            "branch": self.branch,
            "present": list(self.present),
            "missing": list(self.missing),
            "warnings": list(self.warnings),
        }


def _present(value: Any) -> bool:
    """Return True when a bundle item exists."""
    if value is None:
        return False

    if isinstance(value, str):
        return value.strip() != ""

    if isinstance(value, Mapping):
        return bool(value)

    if isinstance(value, list | tuple | set):
        return bool(value)

    return True


def required_keys_for_branch(branch: str) -> tuple[str, ...]:
    """Return required evidence keys for a branch."""
    branch = (branch or "unknown").strip().lower()

    if branch == "gankyil_a":
        return GANKYIL_REQUIRED_KEYS

    if branch in {"plasma_catalyst", "pec", "redox", "hybrid_future"}:
        return ADVANCED_REQUIRED_KEYS

    return BASELINE_REQUIRED_KEYS


def check_bundle(bundle: Mapping[str, Any], *, branch: str | None = None) -> BundleCheck:
    """Check whether a bundle has the required records for its branch."""
    resolved_branch = branch or str(bundle.get("branch") or "baseline")
    required = required_keys_for_branch(resolved_branch)

    present = tuple(key for key in required if _present(bundle.get(key)))
    missing = tuple(key for key in required if key not in present)

    warnings: list[str] = []

    if bundle.get("failed_run") is True and not _present(bundle.get("notes")):
        warnings.append("failed run has no notes")

    if bundle.get("setup_changed_mid_run") is True:
        warnings.append("setup changed mid-run; result may require new run ID")

    if bundle.get("sensor_wetness_observed") is True:
        warnings.append("sensor wetness observed; hydrogen claim should be rejected or downgraded")

    if bundle.get("visual_bubbles_only") is True:
        warnings.append("visual bubbles only are not hydrogen proof")

    complete = not missing
    status = "complete" if complete else "blocked_by_missing_evidence"

    return BundleCheck(
        complete=complete,
        status=status,
        branch=resolved_branch,
        present=present,
        missing=missing,
        warnings=tuple(warnings),
    )


def make_baseline_bundle_template(run_id: str = "GH-A0-YYYYMMDD-001") -> dict[str, Any]:
    """Return an empty baseline evidence bundle template."""
    return {
        "branch": "baseline",
        "run_intent": {
            "run_id": run_id,
            "branch": "baseline",
            "objective": "baseline hydrogen-specific detection under bounded bench conditions",
            "run_duration_limit": "unknown",
        },
        "safety_preflight": {},
        "water_record": {},
        "power_record": {},
        "gas_record": {},
        "carbon_record": {},
        "receipt": {},
        "acceptance": {},
        "notes": "",
        "setup_photos": [],
    }


def make_gankyil_bundle_template(comparison_id: str = "GH-COMP-YYYYMMDD-001") -> dict[str, Any]:
    """Return an empty Gankyil-A comparison bundle template."""
    return {
        "branch": "gankyil_a",
        "comparison_id": comparison_id,
        "baseline_run_reference": {},
        "gankyil_run_reference": {},
        "comparison_conditions": {},
        "phase_management_metrics": {},
        "acceptance": {},
        "notes": "",
        "setup_photos": [],
    }


def missing_evidence_report(bundle: Mapping[str, Any], *, branch: str | None = None) -> dict[str, Any]:
    """Return a reviewer-facing missing evidence report."""
    check = check_bundle(bundle, branch=branch)

    return {
        "branch": check.branch,
        "complete": check.complete,
        "status": check.status,
        "missing_evidence": list(check.missing),
        "present_evidence": list(check.present),
        "warnings": list(check.warnings),
        "review_note": (
            "Evidence bundle is complete enough for acceptance review."
            if check.complete
            else "Evidence bundle is incomplete; claim escalation must be blocked."
        ),
    }


def bundle_file_plan(branch: str = "baseline") -> list[str]:
    """Return recommended file names for a run bundle folder."""
    branch = (branch or "baseline").strip().lower()

    if branch == "gankyil_a":
        return [
            "baseline_run_reference.json",
            "gankyil_run_reference.json",
            "comparison_conditions.json",
            "phase_management_metrics.json",
            "acceptance.json",
            "notes.md",
            "setup_photos/",
        ]

    if branch in {"plasma_catalyst", "pec", "redox", "hybrid_future"}:
        return [
            "run_intent.json",
            "branch_review.json",
            "safety_preflight.json",
            "branch_specific_record.json",
            "water_record.json",
            "power_record.json",
            "gas_record.json",
            "carbon_record.json",
            "receipt.json",
            "acceptance.json",
            "notes.md",
            "setup_photos/",
        ]

    return [
        "run_intent.json",
        "safety_preflight.json",
        "water_record.json",
        "power_record.json",
        "gas_record.json",
        "carbon_record.json",
        "receipt.json",
        "acceptance.json",
        "notes.md",
        "setup_photos/",
    ]


def preserve_failed_run_record(
    *,
    run_id: str,
    branch: str,
    failure_type: str,
    failure_reason: str,
    evidence_present: list[str] | None = None,
    evidence_missing: list[str] | None = None,
    operator_notes: str = "",
) -> dict[str, Any]:
    """Create a minimal failed-run preservation record."""
    return {
        "run_id": run_id,
        "branch": branch,
        "acceptance_status": "rejected",
        "failure_type": failure_type,
        "failure_reason": failure_reason,
        "evidence_present": evidence_present or [],
        "evidence_missing": evidence_missing or [],
        "operator_notes": operator_notes,
        "next_action": "review failure before rerun",
    }
