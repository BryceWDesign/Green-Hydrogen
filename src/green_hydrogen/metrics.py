"""Core metrics for Green-Hydrogen validation.

This module contains conservative helper functions for scoring evidence quality.
The functions do not prove hydrogen production. They only classify whether a
run record contains enough information to support bounded claims.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


UNKNOWN_VALUES = {
    None,
    "",
    "unknown",
    "not_measured",
    "not_applicable",
    "n/a",
    "na",
}


@dataclass(frozen=True)
class EvidenceScore:
    """Small structured score object used by validation helpers."""

    name: str
    score: int
    max_score: int
    status: str
    missing: tuple[str, ...]
    notes: tuple[str, ...]

    @property
    def fraction(self) -> float:
        """Return score as a 0.0-1.0 fraction."""
        if self.max_score <= 0:
            return 0.0
        return self.score / self.max_score

    @property
    def percent(self) -> float:
        """Return score as a percentage."""
        return round(self.fraction * 100.0, 2)


def _is_known(value: Any) -> bool:
    """Return True when a value should count as known evidence."""
    if isinstance(value, str):
        return value.strip().lower() not in UNKNOWN_VALUES
    return value not in UNKNOWN_VALUES


def _missing_fields(record: Mapping[str, Any], required_fields: list[str]) -> tuple[str, ...]:
    """Return required fields that are missing or unknown."""
    return tuple(field for field in required_fields if not _is_known(record.get(field)))


def score_water_record(record: Mapping[str, Any]) -> EvidenceScore:
    """Score water-record completeness.

    Water evidence is mandatory because unknown water weakens interpretation of
    hydrogen output, repeatability, electrode behavior, and contamination risk.
    """

    required = [
        "water_source",
        "water_volume",
        "water_temperature",
        "water_ph",
        "water_tds_or_conductivity",
        "visible_clarity",
    ]

    missing = _missing_fields(record, required)
    score = len(required) - len(missing)

    status = "complete" if not missing else "incomplete"
    notes = []

    if not _is_known(record.get("electrolyte_used")):
        notes.append("electrolyte status is not recorded")

    if record.get("electrolyte_used") is True and not _is_known(
        record.get("electrolyte_source_or_spec")
    ):
        notes.append("electrolyte is used but source/spec is missing")

    return EvidenceScore(
        name="water_record",
        score=score,
        max_score=len(required),
        status=status,
        missing=missing,
        notes=tuple(notes),
    )


def score_power_record(record: Mapping[str, Any]) -> EvidenceScore:
    """Score electrical input evidence.

    Voltage, current, duration, and source are the minimum useful fields.
    Energy/efficiency claims require more than this helper alone.
    """

    required = [
        "source_type",
        "source_description",
        "voltage_v",
        "current_a",
        "duration_s",
        "energy_wh",
        "current_limit_a",
        "fuse_or_protection",
        "emergency_disconnect_confirmed",
        "instrument_used",
    ]

    missing = _missing_fields(record, required)
    score = len(required) - len(missing)

    notes = []

    if not _is_known(record.get("energy_wh")):
        notes.append("energy_wh missing; no energy claim should be accepted")

    if not _is_known(record.get("source_type")):
        notes.append("source_type missing; green-hydrogen claim must be blocked")

    if record.get("emergency_disconnect_confirmed") is not True:
        notes.append("emergency disconnect is not positively confirmed")

    status = "complete" if not missing else "incomplete"

    return EvidenceScore(
        name="power_record",
        score=score,
        max_score=len(required),
        status=status,
        missing=missing,
        notes=tuple(notes),
    )


def score_gas_record(record: Mapping[str, Any]) -> EvidenceScore:
    """Score gas evidence quality.

    Visual bubbles are not hydrogen proof. Hydrogen-specific detection is the
    minimum threshold for a bounded hydrogen claim.
    """

    required = [
        "gas_path_mode",
        "upstream_source",
        "hydrogen_sensor_model",
        "hydrogen_sensor_calibration_state",
        "hydrogen_sensor_initial_state",
        "hydrogen_sensor_final_state",
        "liquid_protection_present",
        "sensor_wetness_observed",
        "oxygen_observation_method",
        "vent_path_defined",
        "leak_check_result",
    ]

    missing = _missing_fields(record, required)
    score = len(required) - len(missing)

    notes = []

    hydrogen_specific = bool(record.get("hydrogen_specific_detection_present"))
    if not hydrogen_specific:
        notes.append("hydrogen-specific detection is missing; hydrogen claim must be blocked")

    if record.get("sensor_wetness_observed") is True:
        notes.append("sensor wetness observed; gas evidence should be rejected or inconclusive")

    if record.get("leak_check_result") not in {"pass", True}:
        notes.append("leak check did not clearly pass")

    if record.get("vent_path_defined") is not True:
        notes.append("vent path not positively confirmed")

    status = "complete" if not missing else "incomplete"

    return EvidenceScore(
        name="gas_record",
        score=score,
        max_score=len(required),
        status=status,
        missing=missing,
        notes=tuple(notes),
    )


def score_carbon_record(record: Mapping[str, Any]) -> EvidenceScore:
    """Score source-traceability and carbon-accounting evidence.

    Hydrogen is not green by default. The source path and renewable fraction must
    be known or honestly bounded before a green-hydrogen claim is considered.
    """

    required = [
        "source_type",
        "source_description",
        "energy_wh",
        "renewable_fraction",
        "battery_used",
        "solar_used",
        "thermal_assist_used",
        "carbon_assumption_note",
    ]

    missing = _missing_fields(record, required)
    score = len(required) - len(missing)

    notes = []

    if str(record.get("source_type", "")).lower() == "unknown":
        notes.append("unknown source blocks green-hydrogen claim")

    if record.get("battery_used") is True and not _is_known(record.get("battery_charge_source")):
        notes.append("battery charge source missing; green-hydrogen claim must be blocked")

    if record.get("thermal_assist_used") is True and not _is_known(
        record.get("thermal_source")
    ):
        notes.append("thermal assist used but thermal source is missing")

    if record.get("thermal_assist_used") is True and not _is_known(
        record.get("thermal_source_temp")
    ):
        notes.append("thermal assist used but thermal source temperature is missing")

    status = "complete" if not missing else "incomplete"

    return EvidenceScore(
        name="carbon_record",
        score=score,
        max_score=len(required),
        status=status,
        missing=missing,
        notes=tuple(notes),
    )


def hydrogen_detection_quality(record: Mapping[str, Any]) -> int:
    """Return hydrogen detection quality level from 0 to 5.

    Levels:
    0 = no gas evidence
    1 = visual bubbles only
    2 = hydrogen-specific detector response, uncalibrated
    3 = hydrogen-specific detector with calibration/bump-test record
    4 = hydrogen sensor plus flow or volume estimate
    5 = repeat calibrated measurements with uncertainty note
    """

    if not record:
        return 0

    if record.get("visual_bubbles_observed") and not record.get(
        "hydrogen_specific_detection_present"
    ):
        return 1

    if not record.get("hydrogen_specific_detection_present"):
        return 0

    calibration_state = str(record.get("hydrogen_sensor_calibration_state", "")).lower()
    bump_state = str(record.get("bump_test_state", "")).lower()

    calibrated = calibration_state in {"pass", "current", "valid", "calibrated"} or bump_state in {
        "pass",
        "current",
        "valid",
    }

    flow_or_volume_present = _is_known(record.get("flow_measurement_method")) or _is_known(
        record.get("gas_volume_estimate")
    )

    repeat_and_uncertainty = bool(record.get("repeat_measurement_present")) and _is_known(
        record.get("uncertainty_note")
    )

    if repeat_and_uncertainty and calibrated and flow_or_volume_present:
        return 5

    if flow_or_volume_present:
        return 4

    if calibrated:
        return 3

    return 2


def energy_accounting_quality(record: Mapping[str, Any]) -> int:
    """Return energy accounting quality level from 0 to 5.

    Levels:
    0 = no power record
    1 = voltage/current observed but not recorded
    2 = voltage/current/duration recorded manually
    3 = watt-hour estimate recorded
    4 = time-series power logged
    5 = power record includes uncertainty and source traceability
    """

    if not record:
        return 0

    if record.get("observed_but_not_recorded") is True:
        return 1

    has_basic = all(
        _is_known(record.get(field)) for field in ("voltage_v", "current_a", "duration_s")
    )
    if not has_basic:
        return 0

    has_energy = _is_known(record.get("energy_wh"))
    has_time_series = bool(record.get("power_time_series_present"))
    has_uncertainty = _is_known(record.get("uncertainty_note"))
    has_source = _is_known(record.get("source_type")) and _is_known(record.get("source_description"))

    if has_time_series and has_uncertainty and has_source:
        return 5

    if has_time_series:
        return 4

    if has_energy:
        return 3

    return 2


def green_hydrogen_claim_quality(record: Mapping[str, Any]) -> int:
    """Return green-hydrogen claim evidence level from 0 to 5.

    Levels:
    0 = no source record
    1 = energy source guessed
    2 = source type recorded
    3 = renewable fraction estimated
    4 = solar/battery/grid path documented
    5 = carbon accounting performed with assumptions
    """

    if not record:
        return 0

    if record.get("source_guessed") is True:
        return 1

    if not _is_known(record.get("source_type")):
        return 0

    if not _is_known(record.get("renewable_fraction")):
        return 2

    source_path_documented = _is_known(record.get("source_description")) and (
        record.get("solar_used") is True
        or record.get("battery_used") is True
        or str(record.get("source_type")).lower() in {"grid", "mixed", "solar", "battery"}
    )

    if not source_path_documented:
        return 3

    if _is_known(record.get("carbon_assumption_note")):
        return 5

    return 4


def gankyil_phase_management_quality(record: Mapping[str, Any]) -> int:
    """Return Gankyil phase-management evidence level from 0 to 5.

    Levels:
    0 = no Gankyil test
    1 = visual swirl observed only
    2 = Gankyil path run without baseline comparison
    3 = A/B comparison completed with notes
    4 = A/B comparison repeated with comparable conditions
    5 = measured reduction in wetting/carryover or improved repeatability
    """

    if not record:
        return 0

    if record.get("visual_swirl_only") is True:
        return 1

    has_gankyil_run = _is_known(record.get("gankyil_run_reference")) or bool(
        record.get("gankyil_run_completed")
    )

    if not has_gankyil_run:
        return 0

    has_baseline = _is_known(record.get("baseline_run_reference"))
    if not has_baseline:
        return 2

    has_comparison_notes = _is_known(record.get("comparison_conditions")) or _is_known(
        record.get("operator_notes")
    )

    if not has_comparison_notes:
        return 2

    repeated = bool(record.get("repeat_comparison_present"))
    measured_improvement = bool(record.get("measured_liquid_carryover_reduction")) or bool(
        record.get("measured_sensor_wetting_reduction")
    ) or bool(record.get("repeatability_improved"))

    if measured_improvement:
        return 5

    if repeated:
        return 4

    return 3


def repeatability_quality(record: Mapping[str, Any]) -> int:
    """Return repeatability evidence level from 0 to 5.

    Levels:
    0 = one incomplete run
    1 = one accepted bounded run
    2 = two comparable runs
    3 = three comparable runs
    4 = three comparable runs with calibrated sensors
    5 = independent replication or external review
    """

    if record.get("independent_replication_present") is True:
        return 5

    comparable_runs = int(record.get("comparable_run_count") or 0)
    calibrated = bool(record.get("calibrated_sensors_used"))

    if comparable_runs >= 3 and calibrated:
        return 4

    if comparable_runs >= 3:
        return 3

    if comparable_runs == 2:
        return 2

    if record.get("accepted_bounded_run_present") is True:
        return 1

    return 0


def evidence_completeness_level(bundle: Mapping[str, Any]) -> int:
    """Return evidence completeness level from 0 to 10.

    This helper uses presence flags and does not inspect file contents.
    """

    if not bundle:
        return 0

    if bundle.get("external_review_packet_present") is True:
        return 9

    if bundle.get("standards_aligned_validation_package_present") is True:
        return 10

    if bundle.get("calibrated_sensors_present") and bundle.get("uncertainty_notes_present"):
        return 8

    if bundle.get("source_traceability_present") and bundle.get("carbon_accounting_present"):
        return 7

    if bundle.get("repeat_runs_present") or bundle.get("ab_comparison_present"):
        return 6

    baseline_files = [
        "run_intent_present",
        "safety_preflight_present",
        "water_record_present",
        "power_record_present",
        "gas_record_present",
        "receipt_present",
        "acceptance_present",
    ]

    if all(bundle.get(field) is True for field in baseline_files):
        return 5

    if bundle.get("gas_record_present") is True:
        return 4

    if bundle.get("water_record_present") and bundle.get("power_record_present"):
        return 3

    if bundle.get("run_intent_present") and bundle.get("safety_preflight_present"):
        return 2

    if bundle.get("run_intent_present"):
        return 1

    return 0


def summarize_scores(scores: list[EvidenceScore]) -> dict[str, Any]:
    """Return a compact summary for a list of evidence scores."""
    if not scores:
        return {
            "overall_percent": 0.0,
            "complete": False,
            "scores": {},
            "missing": {},
            "notes": {},
        }

    total_score = sum(score.score for score in scores)
    total_max = sum(score.max_score for score in scores)

    return {
        "overall_percent": round((total_score / total_max) * 100.0, 2) if total_max else 0.0,
        "complete": all(score.status == "complete" for score in scores),
        "scores": {score.name: score.percent for score in scores},
        "missing": {score.name: list(score.missing) for score in scores if score.missing},
        "notes": {score.name: list(score.notes) for score in scores if score.notes},
    }


def score_baseline_bundle(bundle: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    """Score a baseline evidence bundle.

    Expected keys:
    - water_record
    - power_record
    - gas_record
    - carbon_record
    """

    scores = [
        score_water_record(bundle.get("water_record", {})),
        score_power_record(bundle.get("power_record", {})),
        score_gas_record(bundle.get("gas_record", {})),
        score_carbon_record(bundle.get("carbon_record", {})),
    ]

    summary = summarize_scores(scores)

    gas_record = bundle.get("gas_record", {})
    carbon_record = bundle.get("carbon_record", {})

    summary["hydrogen_detection_quality"] = hydrogen_detection_quality(gas_record)
    summary["energy_accounting_quality"] = energy_accounting_quality(
        bundle.get("power_record", {})
    )
    summary["green_hydrogen_claim_quality"] = green_hydrogen_claim_quality(carbon_record)

    summary["hydrogen_claim_supported"] = (
        gas_record.get("hydrogen_specific_detection_present") is True
        and gas_record.get("sensor_wetness_observed") is not True
        and gas_record.get("leak_check_result") in {"pass", True}
    )

    summary["green_claim_supported"] = (
        summary["hydrogen_claim_supported"] is True
        and green_hydrogen_claim_quality(carbon_record) >= 5
        and _is_known(carbon_record.get("renewable_fraction"))
    )

    return summary
