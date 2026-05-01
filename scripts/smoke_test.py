"""Smoke test runner for Green-Hydrogen.

This script runs a minimal dry validation sequence. It does not operate hardware
and does not prove hydrogen production.
"""

from __future__ import annotations

import json
from pathlib import Path

from green_hydrogen.acceptance import decide_acceptance
from green_hydrogen.evidence_bundle import make_baseline_bundle_template
from green_hydrogen.preflight import passing_dry_baseline_preflight, run_safety_preflight
from green_hydrogen.receipt import create_receipt, receipt_summary_text
from green_hydrogen.state_machine import dry_run_state_sequence


def build_dry_bundle() -> dict:
    """Build a complete dry baseline bundle for smoke testing."""
    bundle = make_baseline_bundle_template("GH-A0-SMOKE-001")

    bundle["run_started"] = True
    bundle["run_completed"] = True

    bundle["run_intent"] = {
        "run_id": "GH-A0-SMOKE-001",
        "branch": "baseline",
        "objective": "dry smoke-test baseline validation",
        "operator": "smoke_test",
        "water_source": "dry_example",
        "power_source": "dry_example",
        "run_duration_limit": "60 seconds",
        "gas_path_mode": "baseline_separator",
        "safety_notes": "dry software smoke test only",
        "pressure_storage_requested": False,
        "flame_test_requested": False,
    }

    preflight = passing_dry_baseline_preflight()
    preflight_result = run_safety_preflight(bundle["run_intent"], preflight)
    bundle["safety_preflight"] = preflight_result.to_record()

    bundle["water_record"] = {
        "water_source": "dry_documented_water",
        "water_volume": "100 mL",
        "water_temperature": 22.0,
        "water_ph": 7.0,
        "water_tds_or_conductivity": "documented",
        "visible_clarity": "clear",
        "electrolyte_used": False,
    }

    bundle["power_record"] = {
        "source_type": "bench_supply",
        "source_description": "dry_current_limited_supply_record",
        "voltage_v": 3.0,
        "current_a": 0.5,
        "duration_s": 60,
        "energy_wh": 0.025,
        "current_limit_a": 1.0,
        "fuse_or_protection": "inline_fuse",
        "emergency_disconnect_confirmed": True,
        "instrument_used": "dry_power_meter_record",
    }

    bundle["gas_record"] = {
        "gas_path_mode": "baseline_separator",
        "upstream_source": "dry_baseline_reference",
        "hydrogen_sensor_model": "dry_hydrogen_specific_detector_record",
        "hydrogen_sensor_calibration_state": "qualitative_only",
        "hydrogen_sensor_initial_state": "ready",
        "hydrogen_sensor_final_state": "response_observed",
        "liquid_protection_present": True,
        "sensor_wetness_observed": False,
        "oxygen_observation_method": "dry_observation_record",
        "vent_path_defined": True,
        "leak_check_result": "pass",
        "hydrogen_specific_detection_present": True,
        "visual_bubbles_observed": True,
    }

    bundle["carbon_record"] = {
        "source_type": "bench_supply",
        "source_description": "not_claimed_renewable",
        "energy_wh": 0.025,
        "renewable_fraction": "unknown",
        "battery_used": False,
        "solar_used": False,
        "thermal_assist_used": False,
        "carbon_assumption_note": "Dry run only. Unknown source blocks green-hydrogen claim.",
    }

    bundle["notes"] = "Dry smoke test only. Not physical evidence."

    receipt = create_receipt(bundle)
    acceptance = decide_acceptance(bundle, branch="baseline")

    bundle["receipt"] = receipt.to_record()
    bundle["acceptance"] = acceptance.to_record()

    return bundle


def main() -> None:
    """Run the dry smoke test and print a compact result."""
    bundle = build_dry_bundle()
    receipt = create_receipt(bundle)
    acceptance = decide_acceptance(bundle, branch="baseline")

    state_record = dry_run_state_sequence(
        run_id="GH-A0-SMOKE-001",
        policy_allowed=True,
        preflight_passed=True,
        evidence_complete=True,
        acceptance_status=acceptance.status,
    )

    output = {
        "smoke_test": "pass" if acceptance.accepted else "fail",
        "receipt": receipt.to_record(),
        "acceptance": acceptance.to_record(),
        "state_machine": state_record,
        "summary": receipt_summary_text(receipt),
        "claim_boundary": "Dry smoke test only. Not physical proof.",
    }

    output_path = Path("run_bundles") / "GH-A0-SMOKE-001-smoke_result.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
