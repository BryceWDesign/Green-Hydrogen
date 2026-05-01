"""Conservative carbon/source accounting helpers for Green-Hydrogen.

This module does not provide default carbon-intensity factors. Users must supply
source-specific factors or mark them unknown. Unknown energy source never counts
as green-hydrogen evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


UNKNOWN = "unknown"


@dataclass(frozen=True)
class CarbonAccountingResult:
    """Bounded source-traceability and carbon-accounting result."""

    source_type: str
    energy_wh: float | None
    renewable_fraction: float | None
    estimated_co2e_g: float | None
    status: str
    green_claim_supported: bool
    reasons: tuple[str, ...]
    assumptions: tuple[str, ...]

    def to_record(self) -> dict[str, Any]:
        """Return a serializable carbon accounting result."""
        return {
            "source_type": self.source_type,
            "energy_wh": self.energy_wh,
            "renewable_fraction": self.renewable_fraction,
            "estimated_co2e_g": self.estimated_co2e_g,
            "status": self.status,
            "green_claim_supported": self.green_claim_supported,
            "reasons": list(self.reasons),
            "assumptions": list(self.assumptions),
        }


def _known(value: Any) -> bool:
    """Return True when a value is meaningfully known."""
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


def _float_or_none(value: Any) -> float | None:
    """Convert value to float when possible."""
    if not _known(value):
        return None

    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def normalize_renewable_fraction(value: Any) -> float | None:
    """Normalize renewable fraction into 0.0-1.0 range.

    Accepts either 0-1 fractions or 0-100 percentages. Values outside range are
    rejected as unknown.
    """
    number = _float_or_none(value)

    if number is None:
        return None

    if 0.0 <= number <= 1.0:
        return number

    if 1.0 < number <= 100.0:
        return number / 100.0

    return None


def estimate_energy_wh(
    *,
    voltage_v: Any,
    current_a: Any,
    duration_s: Any,
) -> float | None:
    """Estimate watt-hours from voltage, current, and seconds."""
    voltage = _float_or_none(voltage_v)
    current = _float_or_none(current_a)
    duration = _float_or_none(duration_s)

    if voltage is None or current is None or duration is None:
        return None

    if voltage < 0 or current < 0 or duration < 0:
        return None

    return (voltage * current * duration) / 3600.0


def estimate_co2e_g(
    *,
    energy_wh: Any,
    grams_co2e_per_kwh: Any,
) -> float | None:
    """Estimate grams CO2e from energy and supplied carbon-intensity factor.

    No default factor is used because grid mix, source, location, date, and
    supplier assumptions matter. The caller must supply the factor.
    """
    energy = _float_or_none(energy_wh)
    factor = _float_or_none(grams_co2e_per_kwh)

    if energy is None or factor is None:
        return None

    if energy < 0 or factor < 0:
        return None

    return (energy / 1000.0) * factor


def evaluate_source_traceability(record: Mapping[str, Any]) -> dict[str, Any]:
    """Evaluate whether an energy source record is traceable enough for claims."""
    source_type = str(record.get("source_type") or UNKNOWN).strip().lower()
    reasons: list[str] = []
    assumptions: list[str] = []

    if source_type == UNKNOWN:
        reasons.append("source_type is unknown")

    if not _known(record.get("source_description")):
        reasons.append("source_description is missing")

    renewable_fraction = normalize_renewable_fraction(record.get("renewable_fraction"))
    if renewable_fraction is None:
        reasons.append("renewable_fraction is unknown or invalid")

    if record.get("battery_used") is True and not _known(record.get("battery_charge_source")):
        reasons.append("battery charge source is missing")

    if record.get("solar_used") is True:
        if not _known(record.get("solar_voltage_v")) and not _known(record.get("voltage_v")):
            reasons.append("solar voltage is not recorded")
        if not _known(record.get("solar_current_a")) and not _known(record.get("current_a")):
            reasons.append("solar current is not recorded")

    if record.get("thermal_assist_used") is True:
        if not _known(record.get("thermal_source")):
            reasons.append("thermal source is missing")
        if not _known(record.get("thermal_source_temp")):
            reasons.append("thermal source temperature is missing")
        assumptions.append("thermal input must be counted before efficiency claims")

    traceable = not reasons

    return {
        "traceable": traceable,
        "source_type": source_type,
        "renewable_fraction": renewable_fraction,
        "reasons": reasons,
        "assumptions": assumptions,
    }


def carbon_accounting_from_records(
    power_record: Mapping[str, Any],
    source_record: Mapping[str, Any],
) -> CarbonAccountingResult:
    """Create a conservative carbon-accounting result from power/source records."""
    reasons: list[str] = []
    assumptions: list[str] = []

    source_eval = evaluate_source_traceability(source_record)
    reasons.extend(source_eval["reasons"])
    assumptions.extend(source_eval["assumptions"])

    energy_wh = _float_or_none(source_record.get("energy_wh"))
    if energy_wh is None:
        energy_wh = _float_or_none(power_record.get("energy_wh"))

    if energy_wh is None:
        energy_wh = estimate_energy_wh(
            voltage_v=power_record.get("voltage_v"),
            current_a=power_record.get("current_a"),
            duration_s=power_record.get("duration_s"),
        )
        if energy_wh is not None:
            assumptions.append("energy_wh estimated from voltage, current, and duration")

    if energy_wh is None:
        reasons.append("energy_wh could not be determined")

    co2e_g = estimate_co2e_g(
        energy_wh=energy_wh,
        grams_co2e_per_kwh=source_record.get("grams_co2e_per_kwh"),
    )

    if co2e_g is None:
        reasons.append("CO2e estimate unavailable because factor or energy is missing")
    else:
        assumptions.append("CO2e estimate uses caller-supplied grams_co2e_per_kwh factor")

    renewable_fraction = source_eval["renewable_fraction"]
    source_type = source_eval["source_type"]

    green_claim_supported = (
        not reasons
        and renewable_fraction is not None
        and renewable_fraction > 0.0
        and energy_wh is not None
        and source_type != UNKNOWN
    )

    if green_claim_supported:
        status = "bounded_source_traceability_supported"
    else:
        status = "green_claim_blocked_or_inconclusive"

    return CarbonAccountingResult(
        source_type=source_type,
        energy_wh=energy_wh,
        renewable_fraction=renewable_fraction,
        estimated_co2e_g=co2e_g,
        status=status,
        green_claim_supported=green_claim_supported,
        reasons=tuple(reasons),
        assumptions=tuple(assumptions),
    )


def carbon_record_template() -> dict[str, Any]:
    """Return a blank carbon/source record template."""
    return {
        "source_type": "unknown",
        "source_description": "unknown",
        "energy_wh": "unknown",
        "renewable_fraction": "unknown",
        "battery_used": False,
        "battery_charge_source": "not_applicable",
        "solar_used": False,
        "solar_voltage_v": "not_applicable",
        "solar_current_a": "not_applicable",
        "thermal_assist_used": False,
        "thermal_source": "not_applicable",
        "thermal_source_temp": "not_applicable",
        "grams_co2e_per_kwh": "unknown",
        "carbon_assumption_note": (
            "Template only. Unknown source cannot support green-hydrogen claim."
        ),
    }


def allowed_carbon_claim(result: CarbonAccountingResult) -> str:
    """Return strongest allowed carbon/source claim."""
    if result.green_claim_supported:
        return (
            "The run has bounded source traceability and a caller-supplied carbon-accounting "
            "basis. This is not a commercial certification."
        )

    return (
        "The run does not support a green-hydrogen claim because source traceability, "
        "renewable fraction, energy, or carbon assumptions are incomplete."
    )
