"""Acceptance validation for Green-Hydrogen runs.

Acceptance maps evidence into bounded claim statuses. It is deliberately
conservative: missing, wet, unsafe, or unsupported evidence fails closed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from .evidence_bundle import check_bundle
from .metrics import green_hydrogen_claim_quality, hydrogen_detection_quality
from .policy import allowed_claims_for_branch, forbidden_claims_for_branch, normalize_branch


ALLOWED_ACCEPTANCE_STATUSES = {
    "accepted_bounded_result",
    "accepted_bounded_phase_management_improvement",
    "accepted_bounded_research_result",
    "rejected",
    "inconclusive",
    "requires_rerun",
    "blocked_by_safety_gate",
    "blocked_by_missing_evidence",
    "blocked_by_missing_baseline",
    "blocked_by_advanced_branch_policy",
}


@dataclass(frozen=True)
class AcceptanceDecision:
    """Final acceptance decision for a run or comparison."""

    accepted: bool
    status: str
    branch: str
    allowed_claims: tuple[str, ...] = field(default_factory=tuple)
    forbidden_claims: tuple[str, ...] = field(default_factory=tuple)
    reasons: tuple[str, ...] = field(default_factory=tuple)
    missing_evidence: tuple[str, ...] = field(default_factory=tuple)
    next_actions: tuple[str, ...] = field(default_factory=tuple)

    def to_record(self) -> dict[str, Any]:
        """Return serializable acceptance decision."""
        return {
            "accepted": self.accepted,
            "status": self.status,
            "branch": self.branch,
            "allowed_claims": list(self.allowed_claims),
            "forbidden_claims": list(self.forbidden_claims),
            "reasons": list(self.reasons),
            "missing_evidence": list(self.missing_evidence),
            "next_actions": list(self.next_actions),
        }


def decide_acceptance(bundle: Mapping[str, Any], *, branch: str | None = None) -> AcceptanceDecision:
    """Return a conservative acceptance decision for a bundle."""
    resolved_branch = normalize_branch(branch or bundle.get("branch") or "baseline")

    if resolved_branch == "gankyil_a":
        return decide_gankyil_acceptance(bundle)

    if resolved_branch in {"plasma_catalyst", "pec", "redox", "hybrid_future"}:
        return decide_advanced_acceptance(bundle, branch=resolved_branch)

    return decide_baseline_acceptance(bundle)


def _preflight_failed(bundle: Mapping[str, Any]) -> bool:
    """Return True if safety preflight clearly failed."""
    preflight = bundle.get("safety_preflight", {})
    if not isinstance(preflight, Mapping):
        return True

    return preflight.get("passed") is False or preflight.get("status") in {
        "blocked_by_safety_gate",
        "blocked_by_policy",
        "blocked_by_advanced_branch_policy",
    }


def decide_baseline_acceptance(bundle: Mapping[str, Any]) -> AcceptanceDecision:
    """Decide acceptance for a baseline run."""
    branch = "baseline"
    check = check_bundle(bundle, branch=branch)

    reasons: list[str] = []
    next_actions: list[str] = []

    if not check.complete:
        return AcceptanceDecision(
            accepted=False,
            status="blocked_by_missing_evidence",
            branch=branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(branch)),
            reasons=("required evidence is missing",),
            missing_evidence=check.missing,
            next_actions=("complete baseline evidence bundle before claim review",),
        )

    if _preflight_failed(bundle):
        return AcceptanceDecision(
            accepted=False,
            status="blocked_by_safety_gate",
            branch=branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(branch)),
            reasons=("safety preflight did not pass",),
            missing_evidence=(),
            next_actions=("resolve safety gate before physical run or claim review",),
        )

    gas = bundle.get("gas_record", {})
    if not isinstance(gas, Mapping):
        gas = {}

    quality = hydrogen_detection_quality(gas)

    if quality <= 1:
        reasons.append("hydrogen-specific detection is missing")
        next_actions.append("use hydrogen-specific detection before hydrogen claim")

    if gas.get("sensor_wetness_observed") is True:
        reasons.append("sensor wetness observed")
        next_actions.append("protect sensor and rerun or mark inconclusive")

    if gas.get("leak_check_result") not in {"pass", True}:
        reasons.append("leak check did not clearly pass")
        next_actions.append("complete leak check before acceptance")

    if gas.get("vent_path_defined") is not True:
        reasons.append("vent path not confirmed")
        next_actions.append("define safe non-pressurized vent path")

    if reasons:
        return AcceptanceDecision(
            accepted=False,
            status="rejected",
            branch=branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(branch)),
            reasons=tuple(reasons),
            missing_evidence=(),
            next_actions=tuple(next_actions),
        )

    return AcceptanceDecision(
        accepted=True,
        status="accepted_bounded_result",
        branch=branch,
        allowed_claims=tuple(allowed_claims_for_branch(branch)),
        forbidden_claims=tuple(forbidden_claims_for_branch(branch)),
        reasons=("baseline evidence supports only a bounded result",),
        missing_evidence=(),
        next_actions=(
            "repeat baseline before repeatability claim",
            "add calibrated measurement before quantitative hydrogen claim",
            "add source traceability and carbon accounting before green-hydrogen claim",
        ),
    )


def decide_gankyil_acceptance(bundle: Mapping[str, Any]) -> AcceptanceDecision:
    """Decide acceptance for Gankyil-A phase-management comparison."""
    branch = "gankyil_a"
    check = check_bundle(bundle, branch=branch)

    if not check.complete:
        return AcceptanceDecision(
            accepted=False,
            status="blocked_by_missing_evidence",
            branch=branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(branch)),
            reasons=("Gankyil comparison evidence is missing",),
            missing_evidence=check.missing,
            next_actions=("complete baseline and Gankyil comparison records",),
        )

    metrics = bundle.get("phase_management_metrics", {})
    if not isinstance(metrics, Mapping):
        metrics = {}

    reasons: list[str] = []
    next_actions: list[str] = []

    if not bundle.get("baseline_run_reference"):
        reasons.append("baseline run reference missing")
        next_actions.append("complete baseline separator run before Gankyil claim")

    if metrics.get("conditions_comparable") is not True:
        reasons.append("comparison conditions are not confirmed comparable")
        next_actions.append("repeat A/B comparison under comparable conditions")

    if metrics.get("restriction_concern") is True:
        reasons.append("restriction concern present")
        next_actions.append("redesign Gankyil path to avoid restriction")

    if metrics.get("sensor_wetness_corrupted") is True:
        reasons.append("sensor wetness corrupted result")
        next_actions.append("improve liquid carryover protection")

    if metrics.get("visual_swirl_only") is True:
        reasons.append("visual swirl alone is not improvement evidence")
        next_actions.append("measure or document practical phase-management metrics")

    improved = metrics.get("phase_management_metric_improved") is True or any(
        metrics.get(field) is True
        for field in (
            "liquid_carryover_reduced",
            "sensor_wetting_reduced",
            "gas_path_stability_improved",
            "condensate_observation_improved",
            "repeatability_improved",
        )
    )

    if not improved:
        reasons.append("no bounded phase-management improvement is documented")
        next_actions.append("repeat comparison or reject Gankyil improvement claim")

    if reasons:
        return AcceptanceDecision(
            accepted=False,
            status="inconclusive" if "no bounded phase-management improvement is documented" in reasons else "rejected",
            branch=branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(branch)),
            reasons=tuple(reasons),
            missing_evidence=(),
            next_actions=tuple(next_actions),
        )

    return AcceptanceDecision(
        accepted=True,
        status="accepted_bounded_phase_management_improvement",
        branch=branch,
        allowed_claims=tuple(allowed_claims_for_branch(branch)),
        forbidden_claims=tuple(forbidden_claims_for_branch(branch)),
        reasons=("Gankyil evidence supports only a bounded phase-management claim",),
        missing_evidence=(),
        next_actions=(
            "repeat A/B comparison before repeatability claim",
            "do not claim hydrogen output or efficiency improvement from this result",
        ),
    )


def decide_advanced_acceptance(
    bundle: Mapping[str, Any],
    *,
    branch: str,
) -> AcceptanceDecision:
    """Decide acceptance for an advanced research branch."""
    resolved_branch = normalize_branch(branch)
    check = check_bundle(bundle, branch=resolved_branch)

    if not check.complete:
        return AcceptanceDecision(
            accepted=False,
            status="blocked_by_missing_evidence",
            branch=resolved_branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(resolved_branch)),
            reasons=("advanced branch evidence bundle is incomplete",),
            missing_evidence=check.missing,
            next_actions=("complete separate branch review and evidence bundle",),
        )

    branch_review = bundle.get("branch_review", {})
    if not isinstance(branch_review, Mapping):
        branch_review = {}

    if branch_review.get("review_status") != "approved":
        return AcceptanceDecision(
            accepted=False,
            status="blocked_by_advanced_branch_policy",
            branch=resolved_branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(resolved_branch)),
            reasons=("advanced branch review is not approved",),
            missing_evidence=(),
            next_actions=("complete formal advanced-branch review before testing",),
        )

    if _preflight_failed(bundle):
        return AcceptanceDecision(
            accepted=False,
            status="blocked_by_safety_gate",
            branch=resolved_branch,
            allowed_claims=(),
            forbidden_claims=tuple(forbidden_claims_for_branch(resolved_branch)),
            reasons=("advanced branch safety preflight did not pass",),
            missing_evidence=(),
            next_actions=("resolve safety gate before any advanced branch run",),
        )

    return AcceptanceDecision(
        accepted=True,
        status="accepted_bounded_research_result",
        branch=resolved_branch,
        allowed_claims=tuple(allowed_claims_for_branch(resolved_branch)),
        forbidden_claims=tuple(forbidden_claims_for_branch(resolved_branch)),
        reasons=("advanced branch supports only a bounded research result",),
        missing_evidence=(),
        next_actions=("preserve branch evidence separately from baseline claims",),
    )


def green_claim_supported(bundle: Mapping[str, Any]) -> bool:
    """Return True only when a bounded green-hydrogen claim has minimum support."""
    gas = bundle.get("gas_record", {})
    carbon = bundle.get("carbon_record", {})

    if not isinstance(gas, Mapping) or not isinstance(carbon, Mapping):
        return False

    return (
        hydrogen_detection_quality(gas) >= 2
        and green_hydrogen_claim_quality(carbon) >= 5
        and carbon.get("renewable_fraction") not in {None, "unknown", "not_measured"}
        and gas.get("sensor_wetness_observed") is not True
    )
