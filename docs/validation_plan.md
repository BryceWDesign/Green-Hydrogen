# Validation Plan

## Purpose

This document defines the validation plan for Green-Hydrogen.

The purpose is to prove or reject bounded claims using measured evidence.

The purpose is not to make the system sound complete before physical data exists.

Green-Hydrogen must treat every claim as unproven until the evidence bundle supports it.

## Validation Target

Target platform:

```
GH-BENCH-A0
```

Primary validation target:
```
A conservative, non-pressurized, supervised bench rig that can produce reviewable evidence for baseline hydrogen detection and later compare Gankyil-A phase-management behavior against a simpler baseline path.
```

Validation Philosophy

The validation plan follows these rules:

Baseline first.
Safety gate before power.
Water record before production claim.
Power record before energy claim.
Hydrogen-specific detection before hydrogen claim.
Energy source record before green-hydrogen claim.
Carbon accounting before low-carbon claim.
Repeat runs before repeatability claim.
A/B evidence before Gankyil improvement claim.
Advanced branches blocked until baseline is stable.
Current Validation Maturity

Current estimate:
```
88-94%
```
Meaning:

The validation architecture is strong, but the project still needs real hardware selection, calibrated sensors, and physical run data.

This score does not mean the system is physically validated.

Validation Levels
Level 0: Repo-Only Validation
Purpose

Confirm the repo is structured enough to support safe planning and evidence discipline.

Evidence Required
project snapshot,
system architecture,
BOM,
safety policy,
hazard register,
validation plan,
test matrix,
example run intent,
safety preflight logic,
evidence bundle logic,
acceptance logic,
smoke tests.

Allowed Claim
```
The validation scaffold can block incomplete or unsafe run intents in dry-run form.
```

Forbidden Claim
```
The physical rig is safe or validated.
```

Level 2: Physical Assembly Validation
Purpose

Confirm the physical bench rig is assembled according to the non-pressurized safety boundary.

Evidence Required
setup photos,
six-zone layout record,
water/electrical separation record,
gas path sketch,
ventilation record,
emergency disconnect record,
leak-check record,
sensor inventory,
component documentation notes,
operator checklist.

Allowed Claim
```
The GH-BENCH-A0 physical layout was assembled for supervised, non-pressurized baseline validation.
```
Forbidden Claim
```
The rig is certified safe.
```

Level 3: Baseline Hydrogen Detection
Purpose

Confirm that the baseline electrolysis reference can produce hydrogen-specific detection under measured bench conditions.

Evidence Required
run intent,
safety preflight,
water record,
power record,
gas path record,
hydrogen detector record,
leak-check record,
operator notes,
post-run inspection,
acceptance decision.

Allowed Claim
```
The GH-BENCH-A0 baseline configuration produced hydrogen-specific detection under documented non-pressurized bench conditions.
```
Forbidden Claim
```
The system produces green hydrogen efficiently.
```

Level 4: Calibrated Baseline Measurement
Purpose

Improve confidence beyond qualitative detection.

Evidence Required
hydrogen sensor model,
calibration or bump-test state,
sensor range,
sensor placement,
gas path record,
flow or volume method if used,
power time-series,
water record,
oxygen-side observation,
uncertainty note,
repeat run.

Allowed Claim
```
The GH-BENCH-A0 baseline configuration produced a bounded hydrogen measurement under documented bench conditions.
```

Forbidden Claim
```
The system has proven commercial output or certified purity.
```

Level 5: Repeat Baseline Runs
Purpose

Test whether the baseline result repeats.

Evidence Required
minimum three comparable baseline runs,
same configuration,
same water source or documented water differences,
similar electrical input,
same sensor placement,
comparable duration,
comparable gas path,
accepted/rejected/inconclusive status for each run,
repeatability summary.

Allowed Claim
```
The baseline hydrogen detection result repeated under comparable GH-BENCH-A0 bench conditions.
```

Forbidden Claim
```
The result is universally repeatable or field-ready.
```

Level 6: Gankyil-A A/B Phase-Management Validation
Purpose

Compare Gankyil-A against a simpler baseline separator path.

Evidence Required
baseline separator run,
Gankyil-A run,
comparable water,
comparable power,
comparable duration,
comparable sensor placement,
liquid carryover observation,
sensor wetness observation,
gas path stability notes,
setup photos,
acceptance decision.

Allowed Claim
```
Gankyil-A improved one or more practical phase-management metrics under tested GH-BENCH-A0 conditions.
```

Forbidden Claim
```
Gankyil-A increases hydrogen production or improves efficiency.
```

Level 7: Solar Electrical Traceability
Purpose

Test whether the energy source can be credibly tied to solar electrical input.

Evidence Required
solar panel or solar-charged battery record,
source path description,
voltage/current measurement,
duration,
battery charge-source record if used,
weather/sky condition,
renewable fraction estimate,
carbon accounting note.

Allowed Claim
```
The run used documented solar-traceable electrical input under bounded bench conditions.
```

Forbidden Claim
```
The system is green hydrogen without carbon accounting and gas evidence.
```

Level 8: Solar Thermal Assist Validation
Purpose

Test whether controlled thermal input changes performance or operating behavior.

Evidence Required
stable baseline reference,
thermal source record,
thermal input temperature,
contact method,
exposure duration,
water/cell temperature,
electrical input,
gas output,
sensor drift notes,
thermal anomaly notes,
acceptance decision.

Allowed Claim
```
A controlled solar thermal assist condition was tested and compared against baseline with measured thermal and electrical records.
```

Forbidden Claim
```
Thermal assist improved efficiency unless total energy accounting supports it.
```
Level 9: Carbon-Traceable Green-Hydrogen Evidence
Purpose

Determine whether a hydrogen run can support a bounded green-hydrogen claim.

Evidence Required
hydrogen measurement,
water input record,
electrical input record,
thermal input record if used,
renewable source record,
carbon accounting,
sensor confidence,
safety preflight,
repeatability evidence,
acceptance result.

Allowed Claim
```
A bounded GH-BENCH-A0 run produced hydrogen with documented renewable-energy traceability and carbon-accounting assumptions.
```

Forbidden Claim
```
The system is net-zero, commercial, or fully validated.
```

Level 10: External Review Package
Purpose

Prepare evidence for external review or replication.

Evidence Required
architecture summary,
BOM,
assembly walkthrough,
hazard register,
validation plan,
raw run evidence,
rejected runs,
accepted runs,
calibration records,
photos,
claim-boundary statement,
reviewer checklist.

Allowed Claim
```
The repo contains a reviewable evidence package for bounded bench-scale validation.
```
Forbidden Claim
```
External review proves field readiness unless reviewers explicitly validate that scope.
```
Validation Sequence

The required validation order is:
```
Level 0: Repo-only validation
  -> Level 1: Dry evidence validation
  -> Level 2: Physical assembly validation
  -> Level 3: Baseline hydrogen detection
  -> Level 4: Calibrated baseline measurement
  -> Level 5: Repeat baseline runs
  -> Level 6: Gankyil-A A/B comparison
  -> Level 7: Solar electrical traceability
  -> Level 8: Solar thermal assist comparison
  -> Level 9: Carbon-traceable green-H2 evidence
  -> Level 10: External review package
```
Do not skip ahead.

Baseline Validation Procedure
Step 1: Create Run Intent

Every run starts with a run intent.

Minimum fields:
```
run_id
operator
branch
objective
water_source
power_source
run_duration_limit
gas_path_mode
sensors_expected
safety_notes
```
Allowed baseline branch:
```
baseline
```
Blocked without review:
```
plasma_catalyst
solar_thermal_assist
pec
redox
unknown
```
Step 2: Complete Safety Preflight

Safety preflight must pass before power.

Required fields:
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
sensor_wetness_protection_confirmed
gas_path_documented
vent_path_defined
branch_selected
run_duration_bounded
prior_anomalies_resolved
evidence_forms_ready
```

If preflight fails, preserve the blocked run.

Step 3: Record Water Evidence

Record:
```
water_source
water_volume
water_temperature
water_ph
water_tds_or_conductivity
visible_clarity
electrolyte_used
electrolyte_source_or_spec
operator_notes
```
No water record means no accepted run.

Step 4: Record Power Evidence

Record:
```
source_type
source_description
voltage_v
current_a
duration_s
energy_wh
current_limit_a
fuse_or_protection
emergency_disconnect_confirmed
instrument_used
operator_notes
```

No power record means no energy or efficiency claim.

Step 5: Record Gas Evidence

Record:
```
gas_path_mode
upstream_source
hydrogen_sensor_model
hydrogen_sensor_calibration_state
hydrogen_sensor_initial_state
hydrogen_sensor_final_state
liquid_protection_present
sensor_wetness_observed
flow_measurement_method
oxygen_observation_method
vent_path_defined
leak_check_result
operator_notes
```

No hydrogen-specific detection means no hydrogen claim.

Step 6: Record Carbon Evidence

Record:
```
source_type
source_description
energy_wh
renewable_fraction
battery_used
battery_charge_source
solar_used
thermal_assist_used
carbon_assumption_note
operator_notes
```
No source traceability means no green-hydrogen claim.

Step 7: Generate Receipt

A receipt should summarize:
```
run_id
branch
preflight_status
water_record_present
power_record_present
gas_record_present
carbon_record_present
safety_status
evidence_status
claim_status
missing_fields
```
Receipts must preserve missing evidence.

Step 8: Acceptance Decision

Acceptance may produce:
```
accepted_bounded_result
accepted_bounded_phase_management_improvement
rejected
inconclusive
requires_rerun
blocked_by_safety_gate
blocked_by_missing_evidence
```
Acceptance must never silently upgrade weak data.

Validation Metrics
Metric 1: Safety Gate Pass/Fail

Question:
```
Did the run pass safety preflight before power?
```

Acceptable values:
```
pass
fail
not_run
```
Metric 2: Evidence Completeness

Question:
```
Were all required evidence files present?
```

Required files:
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
```
Metric 3: Hydrogen Detection Quality

Evidence levels:

Level	Meaning
0	No gas evidence.
1	Visual bubbles only.
2	Hydrogen-specific detector response, uncalibrated.
3	Hydrogen-specific detector with calibration/bump-test record.
4	Hydrogen sensor plus flow or volume estimate.
5	Repeat calibrated measurements with uncertainty note.

Level 1 is not hydrogen proof.

Metric 4: Energy Accounting Quality

Evidence levels:

Level	Meaning
0	No power record.
1	Voltage/current observed but not recorded.
2	Voltage/current/duration recorded manually.
3	Watt-hour estimate recorded.
4	Time-series power logged.
5	Power record includes uncertainty and source traceability.
Metric 5: Green-Hydrogen Claim Quality

Evidence levels:

Level	Meaning
0	No source record.
1	Energy source guessed.
2	Source type recorded.
3	Renewable fraction estimated.
4	Solar/battery/grid path documented.
5	Carbon accounting performed with assumptions.
Metric 6: Gankyil-A Phase-Management Quality

Evidence levels:

Level	Meaning
0	No Gankyil test.
1	Visual swirl observed only.
2	Gankyil path run without baseline comparison.
3	A/B comparison completed with notes.
4	A/B comparison repeated with comparable conditions.
5	Measured reduction in wetting/carryover or improved repeatability.

Visual swirl alone is not proof.

Metric 7: Repeatability

Evidence levels:

Level	Meaning
0	One incomplete run.
1	One accepted bounded run.
2	Two comparable runs.
3	Three comparable runs.
4	Three comparable runs with calibrated sensors.
5	Independent replication or external review.
Baseline Acceptance Criteria

A baseline run can be accepted only if:

safety preflight passed,
ventilation was confirmed,
no pressure storage was present,
no ignition sources were present,
emergency disconnect was present,
leak check passed,
water record was present,
power record was present,
gas path was documented,
hydrogen-specific detection was present,
sensor wetness did not corrupt the reading,
operator notes were recorded,
and evidence bundle was complete enough to review.
Baseline Rejection Criteria

Reject baseline evidence if:

safety preflight failed,
ventilation was missing,
pressure storage was present,
leak check failed,
gas path was unknown,
hydrogen sensor was missing,
visible bubbles were the only evidence,
sensor was wet,
power record was missing,
water record was missing,
evidence folder was missing,
or operator changed the setup mid-run without new run ID.
Gankyil-A Acceptance Criteria

A Gankyil-A improvement claim requires:

valid baseline A-side record,
valid Gankyil B-side record,
comparable water,
comparable power,
comparable duration,
comparable sensor placement,
no safety block,
documented liquid carryover comparison,
documented sensor wetness comparison,
documented gas path stability comparison,
and acceptance status.
Gankyil-A Rejection Criteria

Reject Gankyil-A improvement claim if:

no baseline comparison exists,
conditions are not comparable,
Gankyil path restricts flow,
Gankyil path wets the sensor,
Gankyil path leaks,
guide insert shifts,
evidence is visual swirl only,
or operator cannot explain the gas path.
Solar / Green-Hydrogen Acceptance Criteria

A bounded green-hydrogen claim requires:

hydrogen evidence,
water evidence,
power evidence,
renewable source traceability,
carbon accounting note,
safety preflight,
and acceptance decision.

If hydrogen is detected but energy source is unknown, the run is not green-hydrogen evidence.

If solar is used but not measured, the solar claim is weak or rejected.

If thermal input is used but not counted, efficiency claims are rejected.

Advanced Branch Validation Policy

Advanced branches require separate validation plans.

Advanced branches include:

plasma/catalyst activation,
PEC,
redox-mediated chemistry,
high-temperature thermal assist,
and any unreviewed activation method.

Advanced branches must not be mixed with baseline evidence.

Each advanced branch needs:

separate hazard register section,
separate run intent,
separate safety gate,
separate evidence bundle,
separate acceptance criteria,
and explicit non-claim boundary.
Negative Controls

The validation plan should include negative controls when practical.

Examples:
```
sensor in clean ambient condition before run
water verification before power
gas path dry-state record
power-off sensor baseline
baseline separator before Gankyil-A
uncalibrated sensor marked as qualitative only
solar source unknown marked as unknown
```
Negative controls are not punishment.

They are how the repo avoids fooling itself.

Failed-Run Preservation

Every failed, blocked, or inconclusive run should be preserved.

Required fields:
```
run_id
failure_type
failure_reason
evidence_present
evidence_missing
operator_notes
next_action
```
Do not delete failed runs.

Do not rewrite failed runs as success.

Validation Output Package

A complete validation output package should include:
```
run_bundles/<run_id>/
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
For A/B comparisons:
```
run_bundles/<comparison_id>/
  baseline_run_reference.json
  gankyil_run_reference.json
  comparison_conditions.json
  phase_management_metrics.json
  acceptance.json
  notes.md
  setup_photos/
```
Review Questions

After each run, ask:

Was the run safe enough to accept as evidence?
Was the gas path non-pressurized?
Was hydrogen detected by a hydrogen-specific method?
Was the water source documented?
Was electrical input measured?
Was energy source traceability recorded?
Was carbon accounting possible?
Did sensors behave within their known limits?
Was there liquid carryover?
Was there any wet sensor event?
Was the result repeatable?
Was the claim bounded correctly?
What evidence was missing?
Should the next run be blocked, repeated, or upgraded?
Current Best Validation Claim

The strongest current validation claim before physical data is:
```
Green-Hydrogen defines a safety-gated, evidence-first validation plan for a non-pressurized bench-scale hydrogen proof path, including baseline testing, Gankyil-A phase-management comparison, energy-source traceability, carbon accounting, and acceptance controls.
```

Current Forbidden Validation Claims

Do not claim:
```
Green-Hydrogen has produced verified hydrogen.
Green-Hydrogen has produced verified green hydrogen.
Green-Hydrogen is efficient.
Green-Hydrogen is net-positive.
Green-Hydrogen is safe for unsupervised operation.
Green-Hydrogen is commercially ready.
Gankyil-A improves hydrogen output.
Solar thermal assist improves efficiency.
Plasma/catalyst activation improves performance.
```
Validation Maturity Upgrade Path

To increase validation maturity above 95%, add:

Exact hydrogen sensor model.
Exact oxygen sensor model.
Exact power meter model.
Exact flow or volume method.
Exact water test method.
Calibration checklist.
Sensor uncertainty notes.
Three-run baseline procedure.
Gankyil-A comparison template.
External review checklist.
Final Rule

Validation is not what the repo hopes is true.

Validation is what survives safety gates, measurements, missing-data checks, and conservative acceptance logic.

