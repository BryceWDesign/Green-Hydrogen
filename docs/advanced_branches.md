# Advanced Branches

## Purpose

This document defines the optional advanced research branches for Green-Hydrogen.

These branches are not part of the first baseline proof path.

They exist so the repo can preserve future research directions without confusing them with validated hydrogen evidence.

The advanced branches are:

1. Solar thermal assist.
2. Plasma/catalyst activation.
3. Photoelectrochemical branch.
4. Redox-mediated branch.
5. Future hybrid branch.

## Core Rule

Baseline first.

No advanced branch may be used to claim success until the baseline branch has produced reviewable evidence.

The baseline branch must establish:

- water record,
- power record,
- gas path record,
- hydrogen-specific detection,
- safety preflight,
- leak-check record,
- non-pressurized operation,
- evidence bundle,
- and acceptance decision.

Advanced branches must not be used to rescue a weak baseline.

## Advanced Branch Boundary

Advanced branches are allowed as research directions.

Advanced branches are not allowed as proof shortcuts.

Allowed language:

```
This branch is a future comparison path.
This branch requires separate safety review.
This branch requires separate evidence.
This branch is not validated.
```

Forbidden language:

```
This branch proves higher efficiency.
This branch proves green hydrogen.
This branch makes the system net-positive.
This branch is ready for buildout.
This branch is safe because it is small.
This branch confirms the concept without baseline evidence.
```

## Branch Status Summary

| Branch | Current Status | Default Policy | First Allowed Role |
|---|---|---|---|
| Baseline electrolysis | Primary path | Allowed with safety preflight | First hydrogen-specific detection |
| Gankyil-A phase management | Comparison path | Allowed after baseline characterization | Gas-liquid handling A/B test |
| Solar thermal assist | Optional later | Disabled by default | Controlled thermal comparison |
| Solar electrical input | Optional later | Disabled until source metering exists | Renewable traceability test |
| Plasma/catalyst activation | Blocked | Requires formal review | Separate high-risk research test |
| Photoelectrochemical branch | Future only | Requires separate test article | Solar-to-hydrogen comparison |
| Redox-mediated branch | Future only | Requires separate chemistry review | Decoupled chemistry comparison |
| Hybrid branch | Future only | Requires full architecture review | Multi-input comparison after all single branches |

## Branch Naming

Use branch names exactly.

Allowed branch IDs:

```
baseline
gankyil_a
solar_electrical
solar_thermal_assist
plasma_catalyst
pec
redox
hybrid_future
```

Unknown branch names must be blocked.

## Branch Isolation Rule

Each advanced branch requires its own evidence bundle.

Do not mix branch evidence.

Wrong:

```
Baseline hydrogen detected, so plasma branch improved output.
```

Correct:

```
Baseline branch produced hydrogen-specific detection under documented conditions.
Plasma/catalyst branch remains untested and blocked pending review.
```

## Baseline Branch

## Purpose

The baseline branch is the conservative reference path.

It uses a low-output, documented electrolysis reference module or equivalent conservative hydrogen-generation method.

## Allowed Role

The baseline branch may support the first bounded hydrogen-specific detection claim.

## Required Evidence

```
run_intent.json
safety_preflight.json
water_record.json
power_record.json
gas_record.json
carbon_record.json
receipt.json
acceptance.json
notes.md
setup_photos/
```

## Allowed Claim

```
The GH-BENCH-A0 baseline configuration produced hydrogen-specific detection under documented, non-pressurized bench conditions.
```

## Forbidden Claims

```
The baseline branch proves green hydrogen.
The baseline branch proves efficiency.
The baseline branch proves scale-up.
The baseline branch proves commercial readiness.
```

## Gankyil-A Phase-Management Branch

## Purpose

Gankyil-A is a passive gas-liquid phase-management comparison article.

It tests whether a geometry-guided chamber improves practical gas-liquid handling compared with a simpler baseline separator path.

## Allowed Role

Gankyil-A may support a bounded phase-management claim if A/B comparison evidence supports it.

## Required Prerequisites

- characterized baseline path,
- baseline separator record,
- Gankyil-A installation record,
- comparable water conditions,
- comparable power conditions,
- comparable run duration,
- comparable sensor position,
- leak check,
- non-pressurized path,
- evidence bundle.

## Required Metrics

```
liquid_carryover
sensor_wetting
gas_path_stability
condensate_behavior
restriction_concern
setup_complexity
cleaning_burden
measurement_clarity
```

## Allowed Claim

```
Under GH-BENCH-A0 test conditions, Gankyil-A improved one or more practical phase-management metrics compared with the baseline separator path.
```

## Forbidden Claims

```
Gankyil-A increases hydrogen production.
Gankyil-A improves electrolysis efficiency.
Gankyil-A creates energy.
Gankyil-A proves vortex hydrogen.
Gankyil-A proves green hydrogen.
```

## Solar Electrical Branch

## Purpose

The solar electrical branch tests whether electrical input can be traced to a solar path.

This branch is about source traceability, not automatic green-hydrogen proof.

## Allowed Role

Solar electrical input may support a renewable-source traceability claim only when the energy path is measured and documented.

## Required Prerequisites

- stable baseline evidence,
- solar input hardware selected,
- voltage/current measurement,
- source path record,
- emergency disconnect still present,
- non-pressurized gas path unchanged,
- evidence bundle ready.

## Required Evidence

```
solar_used
panel_description
source_path
voltage_v
current_a
duration_s
energy_wh
battery_used
battery_charge_source
weather_note
renewable_fraction
carbon_assumption_note
```

## Solar Source Cases

## Case 1: Direct Solar Electrical Input

Evidence must record:

- panel description,
- measured voltage,
- measured current,
- run duration,
- sky condition,
- panel orientation if known,
- whether power was buffered,
- and whether input was stable.

## Case 2: Solar-Charged Battery Input

Evidence must record:

- battery used,
- battery charge source,
- charge date if known,
- solar charging evidence,
- battery state if available,
- voltage/current during run,
- and renewable fraction estimate.

## Case 3: Mixed or Unknown Source

If source is mixed or unknown, the run cannot support a clean green-hydrogen claim.

Use:

```
source_type = mixed
```

or:

```
source_type = unknown
```

## Allowed Claim

```
The run used documented solar-traceable electrical input under bounded bench conditions.
```

## Forbidden Claims

```
The run produced green hydrogen solely because solar hardware was nearby.
The battery run was renewable even though battery charge source was unknown.
The system is net-zero.
The system is commercially green.
```

## Solar Thermal Assist Branch

## Purpose

The solar thermal assist branch tests whether controlled thermal input changes system behavior.

Thermal input may affect:

- water temperature,
- electrolysis behavior,
- gas humidity,
- condensation,
- sensor readings,
- material behavior,
- and apparent energy efficiency.

Because of that, thermal input must be measured and counted.

## Default Policy

Solar thermal assist is disabled by default.

It may be tested only after baseline evidence exists.

## Required Prerequisites

- accepted or characterized baseline run,
- thermal source identified,
- thermal input measurement method,
- water or cell temperature measurement,
- sensor drift awareness,
- emergency stop available,
- non-pressurized gas path,
- evidence bundle ready.

## Required Evidence

```
thermal_assist_used
thermal_source
thermal_source_temp
water_temp_start
water_temp_end
cell_surface_temp
ambient_temp
exposure_duration
contact_method
electrical_input
gas_output_evidence
sensor_drift_concern
thermal_anomaly
```

## Thermal Accounting Rule

Thermal input is energy input.

Do not claim efficiency improvement unless thermal energy is included in interpretation.

A run with measured electrical input but unmeasured thermal input cannot support an efficiency claim.

## Allowed Claim

```
A controlled solar thermal assist condition was tested and compared against baseline with measured thermal and electrical records.
```

## Forbidden Claims

```
Solar heat was free, so it does not count.
Thermal assist improved efficiency without measuring thermal input.
Thermal assist proves green hydrogen.
Thermal assist proves net-positive hydrogen.
```

## Solar Thermal Stop Conditions

Stop if:

- temperature rises unexpectedly,
- selected hardware exceeds documented limits,
- tubing softens,
- chamber deforms,
- condensation reaches sensor,
- sensor readings drift unexpectedly,
- power behavior changes unexpectedly,
- gas path becomes unclear,
- or operator safety concern appears.

## Plasma/Catalyst Branch

## Purpose

The plasma/catalyst branch is a speculative high-risk research branch.

It may explore activation effects only under a separate safety envelope.

It is not part of GH-BENCH-A0 baseline testing.

## Default Policy

```
plasma_catalyst = blocked_by_default
```

## Why It Is Blocked

Plasma/catalyst activation may introduce:

- ignition risk,
- high voltage,
- electromagnetic interference,
- sensor corruption,
- ozone or reactive species,
- thermal instability,
- catalyst contamination,
- unknown byproducts,
- and false performance signals.

## Required Before Any Future Review

Before this branch can even be considered, a separate review must define:

- physical separation from baseline path,
- no shared gas accumulation path,
- no pressure storage,
- no ignition exposure,
- high-voltage safety plan,
- EMI isolation plan,
- catalyst material record,
- byproduct monitoring plan,
- sensor shielding or separation,
- emergency shutdown plan,
- and independent acceptance criteria.

## Required Evidence If Ever Tested

```
advanced_branch_review_approved
plasma_source_description
voltage_current_limits
activation_location
gas_path_isolation
catalyst_material_record
byproduct_concern_record
emi_control_record
sensor_interference_check
thermal_record
separate_safety_preflight
separate_gas_record
separate_acceptance_result
```

## Allowed Claim

Only after separate review and evidence:

```
A plasma/catalyst branch condition was tested as a separate research path under its own safety and evidence boundary.
```

## Forbidden Claims

```
Plasma assist improves hydrogen output.
Plasma assist improves efficiency.
Plasma assist is safe because the bench is small.
Plasma assist proves green hydrogen.
Plasma assist may be mixed with baseline evidence.
```

## Plasma/Catalyst Gate

This branch must remain blocked unless all of these are true:

```
advanced_branch_review_approved = true
separate_test_article = true
no_pressure_storage = true
no_shared_claim_with_baseline = true
emi_control_record_present = true
high_voltage_safety_review_present = true
byproduct_review_present = true
operator_review_present = true
```

If any field is false, block the run.

## Photoelectrochemical Branch

## Purpose

The photoelectrochemical branch, or PEC branch, is a future comparison path for light-driven hydrogen production research.

PEC should be treated as a separate test article, not an add-on to the baseline electrolysis rig.

## Default Policy

```
pec = future_only
```

## Why It Is Separate

PEC introduces different proof requirements:

- optical input,
- light intensity,
- material stability,
- electrode/photoabsorber record,
- electrolyte compatibility,
- degradation tracking,
- gas verification,
- and solar-to-hydrogen interpretation.

It cannot borrow baseline electrolysis evidence.

## Required Before PEC Testing

- separate PEC test article,
- material record,
- optical input measurement method,
- water/electrolyte record,
- gas path record,
- hydrogen-specific detection,
- oxygen-side observation,
- degradation tracking,
- and separate acceptance criteria.

## Required Evidence

```
pec_test_article_id
photoabsorber_material
electrode_material
electrolyte_record
light_source
light_intensity_method
exposure_duration
water_record
power_bias_if_any
gas_record
degradation_record
acceptance_result
```

## Allowed Claim

```
A PEC branch condition was documented as a separate research comparison path.
```

## Forbidden Claims

```
PEC proves the baseline works.
PEC proves green hydrogen without source and gas evidence.
PEC output is comparable to baseline without normalized measurement.
PEC material is stable without degradation data.
```

## PEC Gate

PEC testing must be blocked until:

```
separate_test_article = true
optical_input_record_method = true
gas_verification_method = true
material_record = true
degradation_tracking = true
safety_preflight = true
```

## Redox-Mediated Branch

## Purpose

The redox-mediated branch is a future chemistry path that may explore decoupled or buffered hydrogen-production concepts.

It is not part of the first baseline rig.

## Default Policy

```
redox = future_only
```

## Why It Is Separate

Redox-mediated systems may introduce:

- additional chemicals,
- storage ambiguity,
- contamination risk,
- disposal requirements,
- byproduct concerns,
- crossover effects,
- and interpretation complexity.

This branch must not be casually added to baseline water/electrolysis tests.

## Required Before Redox Testing

- separate chemistry review,
- chemical compatibility review,
- safety data review,
- disposal plan,
- storage boundary,
- contamination-control plan,
- separate gas verification,
- separate evidence bundle,
- and separate acceptance criteria.

## Required Evidence

```
redox_test_article_id
redox_mediator_material
chemical_source
concentration
water_record
compatibility_review
disposal_plan
storage_boundary
gas_record
power_record
safety_preflight
acceptance_result
```

## Allowed Claim

```
A redox-mediated branch condition was documented as a separate chemistry research path.
```

## Forbidden Claims

```
Redox branch proves baseline electrolysis performance.
Redox chemistry is safe without review.
Redox branch proves green hydrogen.
Redox branch can be mixed with baseline water records.
```

## Redox Gate

Redox testing must be blocked until:

```
separate_chemistry_review = true
chemical_record_present = true
disposal_plan_present = true
gas_verification_method = true
storage_boundary_defined = true
safety_preflight = true
```

## Hybrid Future Branch

## Purpose

The hybrid future branch is a placeholder for later combinations of validated single branches.

It may include combinations such as:

- baseline plus solar electrical input,
- baseline plus Gankyil-A,
- baseline plus solar thermal assist,
- PEC comparison against baseline,
- or future multi-input comparisons.

## Default Policy

```
hybrid_future = future_only
```

## Hybrid Rule

No hybrid branch may be tested until each single branch in the combination has its own evidence.

Wrong:

```
Test solar thermal, Gankyil-A, and plasma together to see if it works.
```

Correct:

```
Validate baseline first.
Compare Gankyil-A separately.
Test solar electrical traceability separately.
Test solar thermal assist separately.
Only then consider a controlled hybrid comparison.
```

## Hybrid Required Evidence

```
single_branch_evidence_present
combined_run_intent
combined_hazard_review
combined_energy_accounting
combined_gas_record
combined_acceptance_criteria
claim_boundary
```

## Advanced Branch Evidence Bundle

Every advanced branch needs a branch-specific evidence bundle.

Recommended folder:

```
run_bundles/<run_id>/
  run_intent.json
  branch_review.json
  safety_preflight.json
  water_record.json
  power_record.json
  thermal_record.json
  gas_record.json
  carbon_record.json
  branch_specific_record.json
  receipt.json
  acceptance.json
  notes.md
  setup_photos/
```

Files may be omitted only if not applicable, and the omission must be recorded.

Missing evidence must not be hidden.

## Advanced Branch Acceptance States

Advanced branch acceptance may use:

```
blocked_by_advanced_branch_policy
blocked_by_safety_gate
blocked_by_missing_baseline
blocked_by_missing_evidence
rejected
inconclusive
requires_rerun
accepted_bounded_research_result
```

Do not use:

```
proven
validated
commercial_ready
green_hydrogen_confirmed
efficiency_improved
```

unless separate evidence and review support the exact claim.

At the current stage, those stronger terms are not allowed.

## Advanced Branch Safety Gate

Advanced branches must pass all baseline safety requirements plus branch-specific requirements.

Baseline safety requirements:

```
operator_present
ventilation_present
no_pressure_storage
no_sealed_accumulation
no_ignition_sources
emergency_disconnect_present
leak_check_passed
water_electric_separation_confirmed
sensors_connected
gas_path_documented
vent_path_defined
run_duration_bounded
evidence_forms_ready
```

Branch-specific requirements depend on branch type.

## Branch-Specific Gate Summary

| Branch | Extra Required Gate |
|---|---|
| solar_electrical | source path and measured voltage/current |
| solar_thermal_assist | measured thermal input and temperature monitoring |
| plasma_catalyst | formal high-risk review, EMI review, no shared gas path |
| pec | optical input record and separate test article |
| redox | chemistry review and disposal plan |
| hybrid_future | all single-branch evidence already exists |

## Advanced Branch Rejection Rules

Reject advanced branch evidence if:

- baseline evidence is missing,
- branch review is missing,
- safety preflight fails,
- gas path is shared in an unsafe way,
- energy input is hidden,
- thermal input is uncounted,
- sensor data is corrupted,
- chemistry is unknown,
- optical input is unknown,
- EMI risk is ignored,
- or the branch is used to make a claim beyond its evidence.

## Claim Escalation Ladder

Advanced branch evidence should move slowly.

```
branch idea
  -> branch dry review
  -> branch safety review
  -> branch isolated test article
  -> branch bounded observation
  -> branch measured comparison
  -> branch repeat comparison
  -> external review
```

Do not jump from idea to validated claim.

## Current Advanced Branch Maturity

| Branch | Design Maturity | Physical Proof | Notes |
|---|---:|---:|---|
| Solar electrical | Moderate | None | Needs source metering and battery/source records. |
| Solar thermal assist | Moderate | None | Needs thermal measurement and baseline comparison. |
| Plasma/catalyst | Low to moderate | None | Blocked because safety and measurement risks are high. |
| PEC | Low | None | Requires separate test article and optical input evidence. |
| Redox | Low | None | Requires chemistry review and disposal plan. |
| Hybrid future | Low | None | Must wait for single-branch evidence. |

## What Would Raise Advanced Branch Confidence

## Solar Electrical

Confidence rises with:

- measured solar voltage/current,
- battery charge-source record,
- source traceability,
- repeat solar input runs,
- carbon accounting,
- and comparison to grid/bench supply baseline.

## Solar Thermal Assist

Confidence rises with:

- temperature time series,
- measured contact method,
- baseline comparison,
- sensor drift control,
- total energy accounting,
- and repeat runs.

## Plasma/Catalyst

Confidence rises only after:

- formal safety review,
- physical isolation,
- EMI test,
- byproduct review,
- separate sensor path,
- and no shared baseline claim.

## PEC

Confidence rises with:

- known material stack,
- optical input measurement,
- gas verification,
- degradation tracking,
- repeat test,
- and normalized comparison.

## Redox

Confidence rises with:

- documented chemistry,
- compatibility review,
- disposal plan,
- gas verification,
- contamination control,
- and repeatability.

## Advanced Branch Review Template

Before any advanced branch test, create:

```
branch_id:
branch_name:
objective:
why_baseline_is_insufficient:
baseline_run_reference:
new_hazards:
new_sensors_required:
new_energy_inputs:
new_materials:
new_chemistry:
new_stop_conditions:
evidence_files_required:
allowed_claim:
forbidden_claims:
review_status:
reviewer_notes:
```

## Example: Valid Solar Thermal Review Summary

```
branch_id: solar_thermal_assist
objective: Compare baseline run against controlled solar-warmed condition.
baseline_run_reference: GH-A0-YYYYMMDD-001
new_hazards: thermal drift, condensation, material softening.
new_sensors_required: water temperature, ambient temperature, cell surface temperature.
new_energy_inputs: thermal input from solar collector.
new_stop_conditions: unexpected heat, sensor condensation, hardware deformation.
allowed_claim: Controlled thermal assist condition tested against baseline.
forbidden_claims: Efficiency improved, net-positive hydrogen, green hydrogen proven.
review_status: dry_review_only
```

## Example: Blocked Plasma Review Summary

```
branch_id: plasma_catalyst
objective: Explore activation effects.
baseline_run_reference: missing
new_hazards: ignition, high voltage, EMI, reactive species, sensor corruption.
new_sensors_required: undefined
new_energy_inputs: high-voltage activation input
new_stop_conditions: undefined
allowed_claim: none
forbidden_claims: performance improvement, green hydrogen, safe operation.
review_status: blocked_by_advanced_branch_policy
```

## Integration With Evidence Control Plane

Advanced branch requests should pass through:

```
run_intent
  -> branch policy check
  -> safety preflight
  -> evidence requirement check
  -> allowed / blocked decision
  -> receipt
  -> acceptance result
```

If branch policy says blocked, safety preflight should not allow the run.

## Final Rule

Advanced branches are allowed to be ambitious.

They are not allowed to be shortcuts.

A branch earns credibility only when it survives its own safety review, evidence requirements, comparison tests, and claim boundaries.
