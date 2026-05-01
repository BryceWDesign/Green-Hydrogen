"""Conservative validation state machine for Green-Hydrogen.

This state machine describes documentation and evidence states. It does not
operate physical hardware. Unsafe or missing evidence states fail closed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


VALID_STATES = {
    "intent_created",
    "policy_checked",
    "blocked_by_policy",
    "preflight_ready",
    "blocked_by_safety_gate",
    "ready_for_run",
    "run_started",
    "run_stopped",
    "evidence_collected",
    "blocked_by_missing_evidence",
    "acceptance_review",
    "accepted_bounded_result",
    "accepted_bounded_phase_management_improvement",
    "accepted_bounded_research_result",
    "rejected",
    "inconclusive",
    "requires_rerun",
}

TERMINAL_STATES = {
    "blocked_by_policy",
    "blocked_by_safety_gate",
    "blocked_by_missing_evidence",
    "accepted_bounded_result",
    "accepted_bounded_phase_management_improvement",
    "accepted_bounded_research_result",
    "rejected",
    "inconclusive",
    "requires_rerun",
}

ALLOWED_TRANSITIONS = {
    "intent_created": {
        "policy_checked",
        "blocked_by_policy",
    },
    "policy_checked": {
        "preflight_ready",
        "blocked_by_policy",
    },
    "preflight_ready": {
        "ready_for_run",
        "blocked_by_safety_gate",
    },
    "ready_for_run": {
        "run_started",
        "blocked_by_safety_gate",
    },
    "run_started": {
        "run_stopped",
        "rejected",
    },
    "run_stopped": {
        "evidence_collected",
        "blocked_by_missing_evidence",
        "rejected",
        "inconclusive",
    },
    "evidence_collected": {
        "acceptance_review",
        "blocked_by_missing_evidence",
    },
    "acceptance_review": {
        "accepted_bounded_result",
        "accepted_bounded_phase_management_improvement",
        "accepted_bounded_research_result",
        "rejected",
        "inconclusive",
        "requires_rerun",
        "blocked_by_missing_evidence",
    },
}


@dataclass(frozen=True)
class TransitionResult:
    """Result of a requested state transition."""

    allowed: bool
    from_state: str
    to_state: str
    status: str
    reason: str = ""

    def to_record(self) -> dict[str, Any]:
        """Return a serializable transition record."""
        return {
            "allowed": self.allowed,
            "from_state": self.from_state,
            "to_state": self.to_state,
            "status": self.status,
            "reason": self.reason,
        }


@dataclass
class ValidationStateMachine:
    """Simple finite-state machine for validation workflow."""

    run_id: str
    state: str = "intent_created"
    history: list[dict[str, Any]] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate initial state."""
        if self.state not in VALID_STATES:
            raise ValueError(f"invalid initial state: {self.state}")

        if not self.history:
            self.history.append(
                {
                    "run_id": self.run_id,
                    "state": self.state,
                    "event": "init",
                    "reason": "state machine created",
                }
            )

    @property
    def is_terminal(self) -> bool:
        """Return True when current state is terminal."""
        return self.state in TERMINAL_STATES

    def can_transition(self, to_state: str) -> TransitionResult:
        """Check whether a transition is allowed."""
        if to_state not in VALID_STATES:
            return TransitionResult(
                allowed=False,
                from_state=self.state,
                to_state=to_state,
                status="invalid_target_state",
                reason=f"{to_state} is not a recognized state",
            )

        if self.is_terminal:
            return TransitionResult(
                allowed=False,
                from_state=self.state,
                to_state=to_state,
                status="terminal_state",
                reason=f"cannot transition from terminal state {self.state}",
            )

        allowed_targets = ALLOWED_TRANSITIONS.get(self.state, set())

        if to_state not in allowed_targets:
            return TransitionResult(
                allowed=False,
                from_state=self.state,
                to_state=to_state,
                status="transition_not_allowed",
                reason=f"{self.state} cannot transition to {to_state}",
            )

        return TransitionResult(
            allowed=True,
            from_state=self.state,
            to_state=to_state,
            status="allowed",
            reason="transition is allowed",
        )

    def transition(self, to_state: str, *, reason: str = "") -> TransitionResult:
        """Apply a state transition if allowed."""
        result = self.can_transition(to_state)

        if result.allowed:
            self.state = to_state
            self.history.append(
                {
                    "run_id": self.run_id,
                    "state": self.state,
                    "event": "transition",
                    "reason": reason or result.reason,
                }
            )
            return TransitionResult(
                allowed=True,
                from_state=result.from_state,
                to_state=to_state,
                status="transitioned",
                reason=reason or result.reason,
            )

        self.history.append(
            {
                "run_id": self.run_id,
                "state": self.state,
                "event": "blocked_transition",
                "attempted_state": to_state,
                "reason": reason or result.reason,
            }
        )
        return result

    def to_record(self) -> dict[str, Any]:
        """Return serializable state-machine record."""
        return {
            "run_id": self.run_id,
            "state": self.state,
            "is_terminal": self.is_terminal,
            "history": self.history,
        }


def next_state_from_policy(policy_allowed: bool, policy_status: str) -> str:
    """Map policy decision to next state."""
    if policy_allowed:
        return "policy_checked"

    if policy_status.startswith("blocked"):
        return "blocked_by_policy"

    return "blocked_by_policy"


def next_state_from_preflight(preflight_passed: bool) -> str:
    """Map preflight result to next state."""
    return "ready_for_run" if preflight_passed else "blocked_by_safety_gate"


def next_state_from_evidence(evidence_complete: bool) -> str:
    """Map evidence completeness to next state."""
    return "acceptance_review" if evidence_complete else "blocked_by_missing_evidence"


def terminal_state_from_acceptance(acceptance_status: str) -> str:
    """Map acceptance status to terminal state."""
    allowed = {
        "accepted_bounded_result",
        "accepted_bounded_phase_management_improvement",
        "accepted_bounded_research_result",
        "rejected",
        "inconclusive",
        "requires_rerun",
        "blocked_by_safety_gate",
        "blocked_by_missing_evidence",
    }

    if acceptance_status in allowed:
        return acceptance_status

    return "rejected"


def dry_run_state_sequence(
    run_id: str,
    *,
    policy_allowed: bool,
    preflight_passed: bool,
    evidence_complete: bool,
    acceptance_status: str,
) -> dict[str, Any]:
    """Run a dry state-machine sequence for testing."""
    machine = ValidationStateMachine(run_id=run_id)

    policy_next = next_state_from_policy(policy_allowed, "allowed" if policy_allowed else "blocked")
    machine.transition(policy_next, reason="policy check complete")

    if machine.is_terminal:
        return machine.to_record()

    machine.transition("preflight_ready", reason="ready for safety preflight")

    preflight_next = next_state_from_preflight(preflight_passed)
    machine.transition(preflight_next, reason="safety preflight complete")

    if machine.is_terminal:
        return machine.to_record()

    machine.transition("run_started", reason="dry run started")
    machine.transition("run_stopped", reason="dry run stopped")

    evidence_next = next_state_from_evidence(evidence_complete)
    machine.transition(evidence_next, reason="evidence completeness checked")

    if machine.is_terminal:
        return machine.to_record()

    terminal = terminal_state_from_acceptance(acceptance_status)
    machine.transition(terminal, reason="acceptance review complete")

    return machine.to_record()
