from green_hydrogen.carbon_accounting import (
    carbon_accounting_from_records,
    estimate_energy_wh,
    normalize_renewable_fraction,
)
from green_hydrogen.gankyil import (
    check_gankyil_installation,
    compare_phase_management,
    default_gankyil_a0_record,
)
from green_hydrogen.metrics import (
    energy_accounting_quality,
    gankyil_phase_management_quality,
    green_hydrogen_claim_quality,
    hydrogen_detection_quality,
    score_baseline_bundle,
)


def test_hydrogen_detection_quality_blocks_visual_only():
    gas_record = {
        "visual_bubbles_observed": True,
        "hydrogen_specific_detection_present": False,
    }

    assert hydrogen_detection_quality(gas_record) == 1


def test_hydrogen_detection_quality_accepts_hydrogen_specific_detection_level_two():
    gas_record = {
        "visual_bubbles_observed": True,
        "hydrogen_specific_detection_present": True,
        "hydrogen_sensor_calibration_state": "unknown",
    }

    assert hydrogen_detection_quality(gas_record) == 2


def test_energy_accounting_quality_with_watt_hour_estimate():
    power_record = {
        "voltage_v": 3.0,
        "current_a": 0.5,
        "duration_s": 60,
        "energy_wh": 0.025,
        "source_type": "bench_supply",
        "source_description": "current_limited_supply",
    }

    assert energy_accounting_quality(power_record) == 3


def test_green_hydrogen_claim_quality_requires_carbon_note():
    carbon_record = {
        "source_type": "solar",
        "source_description": "documented_direct_solar_path",
        "renewable_fraction": 1.0,
        "solar_used": True,
        "battery_used": False,
        "carbon_assumption_note": "bounded assumption only",
    }

    assert green_hydrogen_claim_quality(carbon_record) == 5


def test_score_baseline_bundle_does_not_support_green_claim_with_unknown_source():
    bundle = {
        "water_record": {
            "water_source": "test_water",
            "water_volume": "100 mL",
            "water_temperature": 22,
            "water_ph": 7,
            "water_tds_or_conductivity": "documented",
            "visible_clarity": "clear",
        },
        "power_record": {
            "source_type": "bench_supply",
            "source_description": "current_limited_supply",
            "voltage_v": 3,
            "current_a": 0.5,
            "duration_s": 60,
            "energy_wh": 0.025,
            "current_limit_a": 1,
            "fuse_or_protection": "inline_fuse",
            "emergency_disconnect_confirmed": True,
            "instrument_used": "inline_power_meter",
        },
        "gas_record": {
            "gas_path_mode": "baseline_separator",
            "upstream_source": "baseline_cell",
            "hydrogen_sensor_model": "test_sensor",
            "hydrogen_sensor_calibration_state": "qualitative_only",
            "hydrogen_sensor_initial_state": "ready",
            "hydrogen_sensor_final_state": "response_observed",
            "liquid_protection_present": True,
            "sensor_wetness_observed": False,
            "oxygen_observation_method": "visual",
            "vent_path_defined": True,
            "leak_check_result": "pass",
            "hydrogen_specific_detection_present": True,
        },
        "carbon_record": {
            "source_type": "unknown",
            "source_description": "unknown",
            "energy_wh": 0.025,
            "renewable_fraction": "unknown",
            "battery_used": False,
            "solar_used": False,
            "thermal_assist_used": False,
            "carbon_assumption_note": "unknown source blocks green claim",
        },
    }

    summary = score_baseline_bundle(bundle)

    assert summary["hydrogen_claim_supported"] is True
    assert summary["green_claim_supported"] is False


def test_estimate_energy_wh_from_voltage_current_duration():
    value = estimate_energy_wh(voltage_v=3.0, current_a=0.5, duration_s=60)

    assert round(value, 6) == 0.025


def test_normalize_renewable_fraction_accepts_percent_and_fraction():
    assert normalize_renewable_fraction(1.0) == 1.0
    assert normalize_renewable_fraction(100) == 1.0
    assert normalize_renewable_fraction(50) == 0.5
    assert normalize_renewable_fraction("unknown") is None


def test_carbon_accounting_blocks_unknown_source():
    power_record = {
        "voltage_v": 3.0,
        "current_a": 0.5,
        "duration_s": 60,
    }
    source_record = {
        "source_type": "unknown",
        "source_description": "unknown",
        "renewable_fraction": "unknown",
        "grams_co2e_per_kwh": "unknown",
    }

    result = carbon_accounting_from_records(power_record, source_record)

    assert result.green_claim_supported is False
    assert result.status == "green_claim_blocked_or_inconclusive"
    assert "source_type is unknown" in result.reasons


def test_gankyil_installation_blocks_template_until_confirmed():
    record = default_gankyil_a0_record()

    result = check_gankyil_installation(record)

    assert result.ready is False
    assert result.status == "blocked"
    assert "non-pressurized operation is not confirmed" in result.blocking_reasons


def test_gankyil_installation_ready_when_required_fields_confirmed():
    record = default_gankyil_a0_record()
    record.update(
        {
            "chamber_transparent_or_inspectable": True,
            "non_pressurized_confirmed": True,
            "outlet_unblocked": True,
            "vent_path_defined": True,
            "leak_check_result": "pass",
            "sensor_wetness_protection_confirmed": True,
        }
    )

    result = check_gankyil_installation(record)

    assert result.ready is True
    assert result.status == "ready_for_bounded_ab_comparison"


def test_gankyil_comparison_accepts_phase_management_only():
    record = {
        "baseline_run_reference": "GH-A0-TEST-001",
        "gankyil_run_reference": "GH-A0-TEST-002",
        "conditions_comparable": True,
        "restriction_concern": False,
        "leak_concern": False,
        "sensor_wetness_corrupted": False,
        "visual_swirl_only": False,
        "liquid_carryover_baseline": "high",
        "liquid_carryover_gankyil": "reduced",
    }

    result = compare_phase_management(record)

    assert result["accepted"] is True
    assert result["status"] == "accepted_bounded_phase_management_improvement"
    assert "reduced_liquid_carryover" in result["bounded_improvements"]
    assert any("increases hydrogen production" in claim for claim in result["forbidden_claims"])


def test_gankyil_phase_management_quality_rejects_visual_swirl_only():
    record = {
        "visual_swirl_only": True,
        "gankyil_run_completed": True,
    }

    assert gankyil_phase_management_quality(record) == 1
