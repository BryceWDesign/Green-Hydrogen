from green_hydrogen.policy import check_branch_policy
from green_hydrogen.preflight import passing_dry_baseline_preflight, run_safety_preflight


def test_baseline_policy_allows_bounded_dry_intent():
    run_intent = {
        "run_id": "GH-A0-TEST-001",
        "branch": "baseline",
        "objective": "dry baseline validation",
        "run_duration_limit": "60 seconds",
        "pressure_storage_requested": False,
        "flame_test_requested": False,
    }

    decision = check_branch_policy(run_intent)

    assert decision.allowed is True
    assert decision.status == "allowed_for_safety_preflight"
    assert decision.branch == "baseline"


def test_unknown_branch_is_blocked():
    run_intent = {
        "run_id": "GH-A0-TEST-002",
        "branch": "mystery_branch",
        "objective": "bad branch test",
        "run_duration_limit": "60 seconds",
    }

    decision = check_branch_policy(run_intent)

    assert decision.allowed is False
    assert decision.status == "blocked_by_unknown_branch"


def test_plasma_branch_is_blocked_without_advanced_review():
    run_intent = {
        "run_id": "GH-BRANCH-TEST-001",
        "branch": "plasma_catalyst",
        "objective": "blocked plasma dry test",
        "run_duration_limit": "not_applicable",
        "advanced_branch_review_approved": False,
        "separate_test_article": False,
        "no_pressure_storage": True,
        "no_shared_claim_with_baseline": False,
        "emi_control_record_present": False,
        "high_voltage_safety_review_present": False,
        "byproduct_review_present": False,
        "operator_review_present": False,
    }

    decision = check_branch_policy(run_intent)

    assert decision.allowed is False
    assert decision.status == "blocked_by_advanced_branch_policy"
    assert decision.branch == "plasma_catalyst"


def test_passing_dry_baseline_preflight_passes():
    run_intent = {
        "run_id": "GH-A0-TEST-003",
        "branch": "baseline",
        "objective": "dry baseline validation",
        "run_duration_limit": "60 seconds",
        "pressure_storage_requested": False,
        "flame_test_requested": False,
    }

    preflight = passing_dry_baseline_preflight()
    result = run_safety_preflight(run_intent, preflight)

    assert result.passed is True
    assert result.status == "pass"
    assert result.failed_fields == ()


def test_preflight_blocks_missing_ventilation():
    run_intent = {
        "run_id": "GH-A0-TEST-004",
        "branch": "baseline",
        "objective": "dry baseline validation",
        "run_duration_limit": "60 seconds",
        "pressure_storage_requested": False,
        "flame_test_requested": False,
    }

    preflight = passing_dry_baseline_preflight()
    preflight["ventilation_present"] = False

    result = run_safety_preflight(run_intent, preflight)

    assert result.passed is False
    assert result.status == "blocked_by_safety_gate"
    assert "ventilation_present" in result.failed_fields
