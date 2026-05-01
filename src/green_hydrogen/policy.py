"""Policy gates for Green-Hydrogen validation.

The policy layer decides whether a run intent is allowed to continue into
safety preflight. It does not operate hardware. It does not prove hydrogen
production. It only blocks unsafe, unsupported, or under-reviewed branches.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


BASELINE_BRANCH = "baseline"

ALLOWED_BRANCHES = {
    "baseline",
    "gankyil_a",
    "solar_electrical",
    "solar_thermal_assist",
    "plasma_catalyst",
    "pec",
    "redox",
    "hybrid_future",
}

BLOCKED_BY_DEFAULT = {
    "plasma_catalyst",
    "pec",
    "redox",
    "hybrid_future",
}

DISABLED_UNTIL_PREREQUISITES = {
    "solar_electrical",
    "solar_thermal_assist",
    "gankyil_a",
}


@dataclass(frozen=True)
class PolicyDecision:
    """Policy decision for a requested run branch."""

    allowed: bool
    status: str
    branch: str
    reasons: tuple[str, ...] = field(default_factory=tuple)
    required_next: tuple[str, ...] = field(default_factory=tuple)

    def to_record(self) -> dict[str, Any]:
        """Return a serializable policy decision."""
        return {
            "allowed": self.allowed,
            "status": self.status,
            "branch": self.branch,
            "reasons": list(self.reasons),
            "required_next": list(self.required_next),
        }


def _known(value: Any) -> bool:
    """Return True if a field is meaningfully known."""
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


def _truthy(record: Mapping[str, Any], field: str) -> bool:
    """Return True only when the field is explicitly true."""
    return record.get(field) is True


def normalize_branch(branch: Any) -> str:
    """Normalize a branch field into the canonical lowercase label."""
    if branch is None:
        return "unknown"

    text = str(branch).strip().lower()
    return text if text else "unknown"


def check_branch_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Check whether a requested branch is allowed by project policy.

    This is intentionally conservative. Unknown branches fail closed.
    """

    branch = normalize_branch(run_intent.get("branch"))

    if branch not in ALLOWED_BRANCHES:
        return PolicyDecision(
            allowed=False,
            status="blocked_by_unknown_branch",
            branch=branch,
            reasons=(f"branch '{branch}' is not recognized",),
            required_next=("select a recognized branch id",),
        )

    if branch == "baseline":
        return _check_baseline_policy(run_intent)

    if branch == "gankyil_a":
        return _check_gankyil_policy(run_intent)

    if branch == "solar_electrical":
        return _check_solar_electrical_policy(run_intent)

    if branch == "solar_thermal_assist":
        return _check_solar_thermal_policy(run_intent)

    if branch == "plasma_catalyst":
        return _check_plasma_policy(run_intent)

    if branch == "pec":
        return _check_pec_policy(run_intent)

    if branch == "redox":
        return _check_redox_policy(run_intent)

    if branch == "hybrid_future":
        return _check_hybrid_policy(run_intent)

    return PolicyDecision(
        allowed=False,
        status="blocked_by_policy",
        branch=branch,
        reasons=("unhandled branch policy path",),
        required_next=("review branch policy implementation",),
    )


def _check_baseline_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Baseline policy: allowed if the intent is bounded and not advanced."""
    reasons: list[str] = []
    required_next: list[str] = []

    if not _known(run_intent.get("run_id")):
        reasons.append("run_id is missing")
        required_next.append("create a stable run_id before preflight")

    if not _known(run_intent.get("objective")):
        reasons.append("objective is missing")
        required_next.append("define a bounded baseline objective")

    if not _known(run_intent.get("run_duration_limit")):
        reasons.append("run_duration_limit is missing")
        required_next.append("define a bounded run duration")

    if run_intent.get("pressure_storage_requested") is True:
        reasons.append("pressure storage requested")
        required_next.append("remove pressure storage from GH-BENCH-A0")

    if run_intent.get("flame_test_requested") is True:
        reasons.append("flame test requested")
        required_next.append("remove flame test; use hydrogen-specific detection")

    allowed = not reasons

    return PolicyDecision(
        allowed=allowed,
        status="allowed_for_safety_preflight" if allowed else "blocked_by_policy",
        branch="baseline",
        reasons=tuple(reasons),
        required_next=tuple(required_next),
    )


def _check_gankyil_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Gankyil policy: allowed only after baseline comparison is defined."""
    reasons: list[str] = []
    required_next: list[str] = []

    if not _known(run_intent.get("baseline_run_reference")):
        reasons.append("baseline_run_reference is missing")
        required_next.append("complete or reference a characterized baseline run")

    if not _known(run_intent.get("comparison_plan")):
        reasons.append("comparison_plan is missing")
        required_next.append("define A/B comparison plan before Gankyil run")

    if run_intent.get("non_pressurized_confirmed") is not True:
        reasons.append("non-pressurized Gankyil path not confirmed")
        required_next.append("confirm Gankyil path is non-pressurized")

    if run_intent.get("production_claim_requested") is True:
        reasons.append("production claim requested from Gankyil branch")
        required_next.append("limit Gankyil claim to phase-management metrics")

    allowed = not reasons

    return PolicyDecision(
        allowed=allowed,
        status="allowed_for_safety_preflight" if allowed else "blocked_by_missing_baseline",
        branch="gankyil_a",
        reasons=tuple(reasons),
        required_next=tuple(required_next),
    )


def _check_solar_electrical_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Solar electrical policy: requires source-path and electrical measurement."""
    reasons: list[str] = []
    required_next: list[str] = []

    if not _known(run_intent.get("source_path")):
        reasons.append("source_path is missing")
        required_next.append("document solar/battery/grid source path")

    if not _truthy(run_intent, "voltage_current_measurement_available"):
        reasons.append("voltage/current measurement not available")
        required_next.append("add voltage/current measurement before solar claim")

    if not _truthy(run_intent, "carbon_record_planned"):
        reasons.append("carbon record not planned")
        required_next.append("prepare carbon/source traceability record")

    allowed = not reasons

    return PolicyDecision(
        allowed=allowed,
        status="allowed_for_safety_preflight" if allowed else "blocked_by_missing_evidence",
        branch="solar_electrical",
        reasons=tuple(reasons),
        required_next=tuple(required_next),
    )


def _check_solar_thermal_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Solar thermal policy: disabled until baseline and thermal evidence exist."""
    reasons: list[str] = []
    required_next: list[str] = []

    if not _known(run_intent.get("baseline_run_reference")):
        reasons.append("baseline_run_reference is missing")
        required_next.append("complete baseline evidence before thermal assist")

    if not _truthy(run_intent, "thermal_record_planned"):
        reasons.append("thermal record not planned")
        required_next.append("prepare thermal input record")

    if not _truthy(run_intent, "temperature_monitoring_available"):
        reasons.append("temperature monitoring not available")
        required_next.append("add water/cell/ambient temperature monitoring")

    if run_intent.get("thermal_input_counted") is not True:
        reasons.append("thermal input is not confirmed counted")
        required_next.append("count thermal input before any efficiency interpretation")

    allowed = not reasons

    return PolicyDecision(
        allowed=allowed,
        status="allowed_for_safety_preflight" if allowed else "blocked_by_missing_evidence",
        branch="solar_thermal_assist",
        reasons=tuple(reasons),
        required_next=tuple(required_next),
    )


def _check_plasma_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Plasma/catalyst policy: blocked by default unless all review gates exist."""
    required = [
        "advanced_branch_review_approved",
        "separate_test_article",
        "no_pressure_storage",
        "no_shared_claim_with_baseline",
        "emi_control_record_present",
        "high_voltage_safety_review_present",
        "byproduct_review_present",
        "operator_review_present",
    ]

    missing = [field for field in required if run_intent.get(field) is not True]

    if missing:
        return PolicyDecision(
            allowed=False,
            status="blocked_by_advanced_branch_policy",
            branch="plasma_catalyst",
            reasons=tuple(f"{field} is not confirmed" for field in missing),
            required_next=(
                "complete separate advanced-branch review before plasma/catalyst testing",
            ),
        )

    return PolicyDecision(
        allowed=True,
        status="allowed_for_safety_preflight",
        branch="plasma_catalyst",
        reasons=(),
        required_next=("maintain separate evidence bundle and no baseline claim mixing",),
    )


def _check_pec_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """PEC policy: future-only until separate test article and optical records exist."""
    required = [
        "separate_test_article",
        "optical_input_record_method",
        "gas_verification_method",
        "material_record",
        "degradation_tracking",
        "safety_preflight",
    ]

    missing = [field for field in required if run_intent.get(field) is not True]

    if missing:
        return PolicyDecision(
            allowed=False,
            status="blocked_by_advanced_branch_policy",
            branch="pec",
            reasons=tuple(f"{field} is not confirmed" for field in missing),
            required_next=("create separate PEC test article and review package",),
        )

    return PolicyDecision(
        allowed=True,
        status="allowed_for_safety_preflight",
        branch="pec",
        reasons=(),
        required_next=("keep PEC evidence separate from baseline electrolysis evidence",),
    )


def _check_redox_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Redox policy: future-only until chemistry review exists."""
    required = [
        "separate_chemistry_review",
        "chemical_record_present",
        "disposal_plan_present",
        "gas_verification_method",
        "storage_boundary_defined",
        "safety_preflight",
    ]

    missing = [field for field in required if run_intent.get(field) is not True]

    if missing:
        return PolicyDecision(
            allowed=False,
            status="blocked_by_advanced_branch_policy",
            branch="redox",
            reasons=tuple(f"{field} is not confirmed" for field in missing),
            required_next=("complete separate redox chemistry and disposal review",),
        )

    return PolicyDecision(
        allowed=True,
        status="allowed_for_safety_preflight",
        branch="redox",
        reasons=(),
        required_next=("keep redox evidence separate from baseline electrolysis evidence",),
    )


def _check_hybrid_policy(run_intent: Mapping[str, Any]) -> PolicyDecision:
    """Hybrid policy: future-only until single-branch evidence exists."""
    required = [
        "single_branch_evidence_present",
        "combined_hazard_review",
        "combined_energy_accounting",
        "combined_gas_record",
        "combined_acceptance_criteria",
    ]

    missing = [field for field in required if run_intent.get(field) is not True]

    if missing:
        return PolicyDecision(
            allowed=False,
            status="blocked_by_advanced_branch_policy",
            branch="hybrid_future",
            reasons=tuple(f"{field} is not confirmed" for field in missing),
            required_next=("validate single branches before hybrid testing",),
        )

    return PolicyDecision(
        allowed=True,
        status="allowed_for_safety_preflight",
        branch="hybrid_future",
        reasons=(),
        required_next=("preserve each branch's evidence boundary inside the hybrid run",),
    )


def allowed_claims_for_branch(branch: str) -> list[str]:
    """Return allowed bounded claim examples for a branch."""
    branch = normalize_branch(branch)

    if branch == "baseline":
        return [
            (
                "GH-BENCH-A0 produced hydrogen-specific detection during a supervised, "
                "non-pressurized baseline bench run with recorded evidence."
            )
        ]

    if branch == "gankyil_a":
        return [
            (
                "Gankyil-A improved one or more practical phase-management metrics "
                "under tested GH-BENCH-A0 conditions."
            )
        ]

    if branch == "solar_electrical":
        return [
            "The run used documented solar-traceable electrical input under bounded conditions."
        ]

    if branch == "solar_thermal_assist":
        return [
            (
                "A controlled solar thermal assist condition was tested and compared "
                "against baseline with measured thermal and electrical records."
            )
        ]

    if branch in {"plasma_catalyst", "pec", "redox", "hybrid_future"}:
        return [
            (
                "A bounded research branch condition was documented under its own "
                "separate safety and evidence boundary."
            )
        ]

    return ["No claim allowed for unknown branch."]


def forbidden_claims_for_branch(branch: str) -> list[str]:
    """Return forbidden claim examples for a branch."""
    common = [
        "The system is commercially ready.",
        "The system is certified safe.",
        "The system is net-positive.",
        "The system is field-ready.",
    ]

    branch = normalize_branch(branch)

    if branch == "baseline":
        return common + [
            "The baseline branch proves green hydrogen.",
            "The baseline branch proves efficiency.",
        ]

    if branch == "gankyil_a":
        return common + [
            "Gankyil-A increases hydrogen production.",
            "Gankyil-A improves electrolysis efficiency.",
            "Gankyil-A creates energy.",
        ]

    if branch == "solar_electrical":
        return common + [
            "Solar hardware nearby proves green hydrogen.",
            "Unknown battery source counts as renewable.",
        ]

    if branch == "solar_thermal_assist":
        return common + [
            "Solar heat was free, so it does not count.",
            "Thermal assist improved efficiency without thermal accounting.",
        ]

    if branch == "plasma_catalyst":
        return common + [
            "Plasma assist improves output.",
            "Plasma assist is safe because the bench is small.",
        ]

    if branch == "pec":
        return common + [
            "PEC proves the baseline works.",
            "PEC material is stable without degradation data.",
        ]

    if branch == "redox":
        return common + [
            "Redox chemistry is safe without review.",
            "Redox branch proves baseline performance.",
        ]

    return common + ["Unknown branch supports a claim."]
