"""Gankyil-A phase-management helpers.

This module does not simulate hydrogen production and does not claim that a
Gankyil geometry improves output. It only provides conservative data structures
and checks for documenting a passive, non-pressurized phase-management test
article used in A/B comparison against a baseline separator path.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


ALLOWED_ORIENTATIONS = {
    "vertical",
    "near_vertical",
    "horizontal",
    "angled",
    "unknown",
}

REQUIRED_GANKYIL_FIELDS = [
    "variant_id",
    "orientation",
    "inlet_position",
    "outlet_position",
    "liquid_collection_position",
    "guide_insert_present",
    "non_pressurized_confirmed",
    "outlet_unblocked",
    "vent_path_defined",
    "leak_check_result",
    "sensor_wetness_protection_confirmed",
]


@dataclass(frozen=True)
class GankyilVariant:
    """Documented Gankyil-A geometry variant.

    The variant record is descriptive. It is not evidence of performance.
    """

    variant_id: str
    orientation: str
    inlet_position: str
    outlet_position: str
    liquid_collection_position: str
    guide_insert_present: bool
    guide_insert_description: str = "not_applicable"
    chamber_material: str = "unknown"
    chamber_transparent_or_inspectable: bool = False
    removable: bool = True
    cleanable: bool = True
    non_pressurized_confirmed: bool = False
    outlet_unblocked: bool = False
    vent_path_defined: bool = False
    notes: str = ""

    def to_record(self) -> dict[str, Any]:
        """Return a serializable record."""
        return {
            "variant_id": self.variant_id,
            "orientation": self.orientation,
            "inlet_position": self.inlet_position,
            "outlet_position": self.outlet_position,
            "liquid_collection_position": self.liquid_collection_position,
            "guide_insert_present": self.guide_insert_present,
            "guide_insert_description": self.guide_insert_description,
            "chamber_material": self.chamber_material,
            "chamber_transparent_or_inspectable": self.chamber_transparent_or_inspectable,
            "removable": self.removable,
            "cleanable": self.cleanable,
            "non_pressurized_confirmed": self.non_pressurized_confirmed,
            "outlet_unblocked": self.outlet_unblocked,
            "vent_path_defined": self.vent_path_defined,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class GankyilCheckResult:
    """Result from checking Gankyil-A readiness."""

    ready: bool
    status: str
    missing_fields: tuple[str, ...] = field(default_factory=tuple)
    blocking_reasons: tuple[str, ...] = field(default_factory=tuple)
    warnings: tuple[str, ...] = field(default_factory=tuple)

    def to_record(self) -> dict[str, Any]:
        """Return a serializable check result."""
        return {
            "ready": self.ready,
            "status": self.status,
            "missing_fields": list(self.missing_fields),
            "blocking_reasons": list(self.blocking_reasons),
            "warnings": list(self.warnings),
        }


@dataclass(frozen=True)
class PhaseComparison:
    """A/B comparison record for baseline separator versus Gankyil-A.

    This record supports bounded phase-management review only. It must not be
    used as hydrogen-output or efficiency proof.
    """

    comparison_id: str
    baseline_run_reference: str
    gankyil_run_reference: str
    conditions_comparable: bool
    liquid_carryover_baseline: str = "unknown"
    liquid_carryover_gankyil: str = "unknown"
    sensor_wetting_baseline: str = "unknown"
    sensor_wetting_gankyil: str = "unknown"
    gas_path_stability_baseline: str = "unknown"
    gas_path_stability_gankyil: str = "unknown"
    condensate_behavior_baseline: str = "unknown"
    condensate_behavior_gankyil: str = "unknown"
    restriction_concern: bool = False
    leak_concern: bool = False
    operator_notes: str = ""

    def to_record(self) -> dict[str, Any]:
        """Return a serializable comparison record."""
        return {
            "comparison_id": self.comparison_id,
            "baseline_run_reference": self.baseline_run_reference,
            "gankyil_run_reference": self.gankyil_run_reference,
            "conditions_comparable": self.conditions_comparable,
            "liquid_carryover_baseline": self.liquid_carryover_baseline,
            "liquid_carryover_gankyil": self.liquid_carryover_gankyil,
            "sensor_wetting_baseline": self.sensor_wetting_baseline,
            "sensor_wetting_gankyil": self.sensor_wetting_gankyil,
            "gas_path_stability_baseline": self.gas_path_stability_baseline,
            "gas_path_stability_gankyil": self.gas_path_stability_gankyil,
            "condensate_behavior_baseline": self.condensate_behavior_baseline,
            "condensate_behavior_gankyil": self.condensate_behavior_gankyil,
            "restriction_concern": self.restriction_concern,
            "leak_concern": self.leak_concern,
            "operator_notes": self.operator_notes,
        }


def _known(value: Any) -> bool:
    """Return True when a value is present and not an unknown placeholder."""
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


def missing_gankyil_fields(record: Mapping[str, Any]) -> tuple[str, ...]:
    """Return missing required fields for a Gankyil-A installation record."""
    return tuple(field for field in REQUIRED_GANKYIL_FIELDS if not _known(record.get(field)))


def check_gankyil_installation(record: Mapping[str, Any]) -> GankyilCheckResult:
    """Check whether a Gankyil-A installation is ready for A/B testing.

    This check is intentionally conservative. If the setup could create pressure,
    wet the sensor, or hide the gas path, it is not ready.
    """

    missing = missing_gankyil_fields(record)
    blocking: list[str] = []
    warnings: list[str] = []

    orientation = str(record.get("orientation", "unknown")).strip().lower()
    if orientation not in ALLOWED_ORIENTATIONS:
        warnings.append(f"orientation '{orientation}' is not in allowed orientation labels")

    if record.get("non_pressurized_confirmed") is not True:
        blocking.append("non-pressurized operation is not confirmed")

    if record.get("outlet_unblocked") is not True:
        blocking.append("outlet is not confirmed unblocked")

    if record.get("vent_path_defined") is not True:
        blocking.append("vent path is not defined")

    if record.get("leak_check_result") not in {"pass", True}:
        blocking.append("leak check did not clearly pass")

    if record.get("sensor_wetness_protection_confirmed") is not True:
        blocking.append("sensor wetness protection is not confirmed")

    if record.get("chamber_transparent_or_inspectable") is not True:
        warnings.append("chamber is not confirmed transparent or inspectable")

    if record.get("removable") is False:
        warnings.append("Gankyil chamber is not removable; baseline comparison may be harder")

    if record.get("cleanable") is False:
        warnings.append("Gankyil chamber is not cleanable; repeatability may be weak")

    if record.get("guide_insert_present") is True and not _known(
        record.get("guide_insert_description")
    ):
        warnings.append("guide insert is present but not described")

    ready = not missing and not blocking

    if ready:
        status = "ready_for_bounded_ab_comparison"
    elif blocking:
        status = "blocked"
    else:
        status = "incomplete"

    return GankyilCheckResult(
        ready=ready,
        status=status,
        missing_fields=missing,
        blocking_reasons=tuple(blocking),
        warnings=tuple(warnings),
    )


def compare_phase_management(record: Mapping[str, Any]) -> dict[str, Any]:
    """Evaluate a Gankyil-A A/B comparison at a bounded evidence level.

    The output is not a production-performance claim. It only indicates whether
    the comparison supports a possible phase-management improvement.
    """

    missing: list[str] = []

    for field_name in (
        "baseline_run_reference",
        "gankyil_run_reference",
        "conditions_comparable",
    ):
        if not _known(record.get(field_name)):
            missing.append(field_name)

    blocking: list[str] = []

    if record.get("conditions_comparable") is not True:
        blocking.append("conditions are not confirmed comparable")

    if record.get("restriction_concern") is True:
        blocking.append("restriction concern present")

    if record.get("leak_concern") is True:
        blocking.append("leak concern present")

    if record.get("sensor_wetness_corrupted") is True:
        blocking.append("sensor wetness corrupted the run")

    if record.get("visual_swirl_only") is True:
        blocking.append("visual swirl alone is not evidence of improvement")

    improvements = detect_phase_management_improvements(record)

    accepted = not missing and not blocking and bool(improvements)

    if accepted:
        status = "accepted_bounded_phase_management_improvement"
    elif missing:
        status = "blocked_by_missing_evidence"
    elif blocking:
        status = "rejected"
    else:
        status = "inconclusive"

    return {
        "accepted": accepted,
        "status": status,
        "missing_evidence": missing,
        "blocking_reasons": blocking,
        "bounded_improvements": improvements,
        "allowed_claim": allowed_gankyil_claim(improvements),
        "forbidden_claims": forbidden_gankyil_claims(),
    }


def detect_phase_management_improvements(record: Mapping[str, Any]) -> list[str]:
    """Return bounded phase-management improvements supported by the record."""

    improvements: list[str] = []

    liquid_base = str(record.get("liquid_carryover_baseline", "")).strip().lower()
    liquid_gank = str(record.get("liquid_carryover_gankyil", "")).strip().lower()

    wet_base = str(record.get("sensor_wetting_baseline", "")).strip().lower()
    wet_gank = str(record.get("sensor_wetting_gankyil", "")).strip().lower()

    stability_base = str(record.get("gas_path_stability_baseline", "")).strip().lower()
    stability_gank = str(record.get("gas_path_stability_gankyil", "")).strip().lower()

    condensate_base = str(record.get("condensate_behavior_baseline", "")).strip().lower()
    condensate_gank = str(record.get("condensate_behavior_gankyil", "")).strip().lower()

    if liquid_base in {"high", "moderate", "observed", "yes"} and liquid_gank in {
        "low",
        "none",
        "reduced",
        "improved",
    }:
        improvements.append("reduced_liquid_carryover")

    if wet_base in {"yes", "observed", "risk", "wet"} and wet_gank in {
        "no",
        "none",
        "dry",
        "reduced",
    }:
        improvements.append("reduced_sensor_wetting")

    if stability_base in {"unstable", "pulsing", "inconsistent", "poor"} and stability_gank in {
        "stable",
        "improved",
        "consistent",
    }:
        improvements.append("improved_gas_path_stability")

    if condensate_base in {"unclear", "hard_to_observe", "messy"} and condensate_gank in {
        "clear",
        "easier_to_observe",
        "improved",
    }:
        improvements.append("improved_condensate_observation")

    if record.get("repeatability_improved") is True:
        improvements.append("improved_repeatability")

    if record.get("cleaning_burden_reduced") is True:
        improvements.append("reduced_cleaning_burden")

    return improvements


def allowed_gankyil_claim(improvements: list[str]) -> str:
    """Return the strongest allowed bounded Gankyil claim."""
    if not improvements:
        return (
            "No Gankyil-A improvement claim is supported. The result is rejected, "
            "inconclusive, or requires rerun."
        )

    return (
        "Under GH-BENCH-A0 test conditions, Gankyil-A improved one or more "
        "practical phase-management metrics compared with the baseline separator path."
    )


def forbidden_gankyil_claims() -> list[str]:
    """Return forbidden Gankyil claim wording."""
    return [
        "Gankyil-A increases hydrogen production.",
        "Gankyil-A improves electrolysis efficiency.",
        "Gankyil-A creates energy.",
        "Gankyil-A proves vortex-enhanced hydrogen generation.",
        "Gankyil-A proves green hydrogen.",
        "Gankyil-A is validated for field deployment.",
    ]


def default_gankyil_a0_record() -> dict[str, Any]:
    """Return a conservative default record template for Gankyil-A0."""
    return {
        "variant_id": "GANKYIL-A0",
        "orientation": "vertical",
        "orientation_angle_degrees": 90,
        "inlet_position": "lower_side",
        "outlet_position": "upper_side_or_upper_center",
        "liquid_collection_position": "lower_region",
        "guide_insert_present": False,
        "guide_insert_description": "not_applicable",
        "chamber_material": "unknown",
        "chamber_transparent_or_inspectable": False,
        "removable": True,
        "cleanable": True,
        "non_pressurized_confirmed": False,
        "outlet_unblocked": False,
        "vent_path_defined": False,
        "leak_check_result": "not_measured",
        "sensor_wetness_protection_confirmed": False,
        "notes": "Template only. Not physical proof.",
    }


def gankyil_ab_template() -> dict[str, Any]:
    """Return an A/B comparison template."""
    return {
        "comparison_id": "GH-COMP-YYYYMMDD-001",
        "baseline_run_reference": "unknown",
        "gankyil_run_reference": "unknown",
        "conditions_comparable": False,
        "liquid_carryover_baseline": "unknown",
        "liquid_carryover_gankyil": "unknown",
        "sensor_wetting_baseline": "unknown",
        "sensor_wetting_gankyil": "unknown",
        "gas_path_stability_baseline": "unknown",
        "gas_path_stability_gankyil": "unknown",
        "condensate_behavior_baseline": "unknown",
        "condensate_behavior_gankyil": "unknown",
        "restriction_concern": False,
        "leak_concern": False,
        "sensor_wetness_corrupted": False,
        "visual_swirl_only": False,
        "repeatability_improved": False,
        "cleaning_burden_reduced": False,
        "operator_notes": "Template only. Not physical proof.",
    }
