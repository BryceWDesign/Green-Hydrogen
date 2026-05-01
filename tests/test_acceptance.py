from green_hydrogen.acceptance import decide_acceptance, green_claim_supported
from green_hydrogen.evidence_bundle import check_bundle, make_baseline_bundle_template
from green_hydrogen.receipt import create_receipt, receipt_summary_text


def complete_baseline_bundle():
    return {
        "branch": "baseline",
        "run_started": True,
        "run_completed": True,
        "run_intent": {
            "run_id": "GH-A0-TEST-ACCEPT-001",
            "branch": "baseline",
            "objective": "bounded baseline dry acceptance",
            "operator": "test_operator",
            "run_duration_limit": "60 seconds",
            "gas_path_mode": "baseline_separator",
            "safety_notes": "dry test only",
        },
        "safety_preflight": {
            "passed": True,
            "status": "pass",
        },
        "water_record": {
            "water_source": "documented_test_water",
            "water_volume": "100 mL",
            "water_temperature": 22.0,
            "water_ph": 7.0,
            "water_tds_or_conductivity": "documented",
            "visible_clarity": "clear",
            "electrolyte_used": False,
        },
        "power_record": {
            "source_type": "bench_supply",
            "source_description": "current_limited_dc_supply",
            "voltage_v": 3.0,
            "current_a": 0.5,
            "duration_s": 60,
            "energy_wh": 0.025,
            "current_limit_a": 1.0,
            "fuse_or_protection": "inline_fuse",
            "emergency_disconnect_confirmed": True,
            "instrument_used": "inline_power_meter",
        },
        "gas_record": {
            "gas_path_mode": "baseline_separator",
            "upstream_source": "baseline_electrolysis_reference",
            "hydrogen_sensor_model": "documented_test_sensor",
            "hydrogen_sensor_calibration_state": "qualitative_only",
            "hydrogen_sensor_initial_state": "ready",
            "hydrogen_sensor_final_state": "response_observed",
            "liquid_protection_present": True,
            "sensor_wetness_observed": False,
            "oxygen_observation_method": "visual_or_sensor_record",
            "vent_path_defined": True,
            "leak_check_result": "pass",
            "hydrogen_specific_detection_present": True,
            "visual_bubbles_observed": True,
        },
        "carbon_record": {
            "source_type": "bench_supply",
            "source_description": "grid_or_lab_supply_not_claimed_green",
            "energy_wh": 0.025,
            "renewable_fraction": "unknown",
            "battery_used": False,
            "solar_used": False,
            "thermal_assist_used": False,
            "carbon_assumption_note": "Not a green-hydrogen claim.",
        },
        "receipt": {
            "claim_status": "accepted_bounded_result",
        },
        "acceptance": {
            "status": "pending_review",
        },
        "notes": "Dry acceptance test only. Not physical evidence.",
    }


def test_complete_baseline_bundle_checks_complete():
    bundle = complete_baseline_bundle()

    check = check_bundle(bundle, branch="baseline")

    assert check.complete is True
    assert check.status == "complete"
    assert check.missing == ()


def test_baseline_acceptance_accepts_bounded_result():
    bundle = complete_baseline_bundle()

    decision = decide_acceptance(bundle, branch="baseline")

    assert decision.accepted is True
    assert decision.status == "accepted_bounded_result"
    assert decision.branch == "baseline"
    assert any("GH-BENCH-A0" in claim for claim in decision.allowed_claims)


def test_baseline_acceptance_rejects_visual_bubbles_only():
    bundle = complete_baseline_bundle()
    bundle["gas_record"]["hydrogen_specific_detection_present"] = False

    decision = decide_acceptance(bundle, branch="baseline")

    assert decision.accepted is False
    assert decision.status == "rejected"
    assert "hydrogen-specific detection is missing" in decision.reasons


def test_baseline_acceptance_blocks_missing_evidence():
    bundle = make_baseline_bundle_template("GH-A0-TEST-MISSING-001")

    decision = decide_acceptance(bundle, branch="baseline")

    assert decision.accepted is False
    assert decision.status == "blocked_by_missing_evidence"
    assert decision.missing_evidence


def test_green_claim_not_supported_when_source_unknown():
    bundle = complete_baseline_bundle()

    assert green_claim_supported(bundle) is False


def test_receipt_preserves_bounded_claim_status():
    bundle = complete_baseline_bundle()

    receipt = create_receipt(bundle)
    summary = receipt_summary_text(receipt)

    assert receipt.run_id == "GH-A0-TEST-ACCEPT-001"
    assert receipt.claim_status == "accepted_bounded_result"
    assert "does not prove green hydrogen" in summary
