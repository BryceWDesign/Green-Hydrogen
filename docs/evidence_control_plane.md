# Evidence Control Plane

## Purpose

The Green-Hydrogen evidence control plane defines how run intent, safety preflight, measurement records, receipts, acceptance decisions, and claim boundaries flow through the repo.

The goal is to make every result reviewable.

The evidence control plane exists to prevent:

- unsafe run approval,
- missing evidence acceptance,
- unsupported green-hydrogen claims,
- visual-only hydrogen claims,
- untracked advanced-branch claims,
- deleted failed runs,
- and inflated maturity scoring.

## Core Principle

A claim is not accepted because the operator believes it.

A claim is accepted only if the evidence bundle supports a bounded result.

If evidence is missing, the claim is blocked, rejected, or marked inconclusive.

## Control Plane Summary

```
run_intent.json
  -> branch_policy_check
  -> safety_preflight
  -> evidence_requirement_check
  -> run_execution_or_block
  -> measurement_records
  -> receipt
  -> acceptance
  -> claim_boundary
  -> run_bundle
```

Primary Inputs

The evidence control plane accepts these inputs:

Input	Purpose
run_intent.json	Defines what the operator plans to do.
safety_preflight.json	Confirms whether the run is allowed before power.
water_record.json	Documents water source and condition.
power_record.json	Documents electrical input and source.
gas_record.json	Documents gas path and hydrogen evidence.
thermal_record.json	Documents thermal input if used.
carbon_record.json	Documents source traceability and carbon assumptions.
branch_review.json	Required for advanced branches.
notes.md	Preserves operator observations and anomalies.
setup_photos/	Preserves layout and hardware evidence.
Primary Outputs

The evidence control plane produces these outputs:

Output	Purpose
receipt.json	Summarizes what happened and what evidence exists.
acceptance.json	Gives accepted, rejected, blocked, or inconclusive status.
missing_evidence	Lists required evidence that was not present.
claim_status	Defines what can and cannot be said.
review_notes	Gives reviewer-facing explanation.
Run Bundle Structure

Recommended run bundle:
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

Optional files:
```
run_bundles/<run_id>/
  thermal_record.json
  branch_review.json
  phase_management_metrics.json
  calibration_record.json
  sensor_log.csv
  manual_log_scan.jpg
```

Run ID Standard

Recommended run ID format:
```
GH-A0-YYYYMMDD-001
```
Examples:
```
GH-A0-20260429-001
GH-A0-20260429-002
GH-A0-20260430-001
```
Comparison bundle format:
```
GH-COMP-YYYYMMDD-001
```
Advanced branch format:
```
GH-BRANCH-YYYYMMDD-001
```
Run ID Rules

Run IDs must be:

unique,
timestamped,
stable after creation,
referenced in every evidence file,
and never reused after a failed run.

Do not rename a failed run to make the record look cleaner.

Do not reuse a run ID because the first attempt failed.

Branch Policy

Every run must declare a branch.

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

Unknown branch IDs must be blocked.

Branch Default States
Branch	Default State	Reason
baseline	allowed with safety preflight	Primary conservative path.
gankyil_a	allowed after baseline characterization	Phase-management comparison only.
solar_electrical	disabled until source metering exists	Requires source traceability.
solar_thermal_assist	disabled until baseline stable	Requires thermal accounting.
plasma_catalyst	blocked by default	Ignition, EMI, high-voltage, byproduct risk.
pec	future only	Requires separate test article.
redox	future only	Requires chemistry review.
hybrid_future	future only	Requires single-branch evidence first.

Branch Policy Logic
```
if branch == baseline:
    allow policy review to continue

elif branch == gankyil_a:
    require baseline_run_reference
    require comparison_plan
    require non_pressurized_confirmation

elif branch == solar_electrical:
    require source_path
    require voltage_current_measurement
    require carbon_record

elif branch == solar_thermal_assist:
    require baseline_run_reference
    require thermal_record
    require temperature_monitoring

elif branch == plasma_catalyst:
    block unless advanced_branch_review_approved

elif branch == pec:
    block unless separate_test_article and optical_input_record exist

elif branch == redox:
    block unless separate_chemistry_review and disposal_plan exist

elif branch == hybrid_future:
    block unless all included single branches have evidence

else:
    block unknown branch
```
Safety Preflight Gate

Safety preflight happens before any physical run.

Required safety fields:
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
Safety Gate Pass Rule

A run may proceed only if all required safety fields pass.

Safety pass means:
```
safety_preflight_status = pass
```

Safety fail means:
```
safety_preflight_status = fail
acceptance_status = blocked_by_safety_gate
```

Automatic Safety Blocks

Block the run if any of these are true:
```
ventilation_present = false
no_pressure_storage = false
no_sealed_accumulation = false
no_ignition_sources = false
emergency_disconnect_present = false
leak_check_passed = false
water_electric_separation_confirmed = false
sensors_connected = false
gas_path_documented = false
vent_path_defined = false
run_duration_bounded = false
operator_present = false
```

Evidence Requirement Gate

After safety preflight, the system checks whether the run has the evidence files required for the selected branch.

Baseline required files:
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

Gankyil-A comparison required files:
```
baseline_run_reference.json
gankyil_run_reference.json
comparison_conditions.json
phase_management_metrics.json
acceptance.json
notes.md
setup_photos/
```
Solar thermal required files:
```
thermal_record.json
power_record.json
gas_record.json
carbon_record.json
acceptance.json
notes.md
```
Advanced branch required files:
```
branch_review.json
safety_preflight.json
branch_specific_record.json
gas_record.json
power_record.json
acceptance.json
notes.md
```
Missing Evidence Rule

Missing evidence must be preserved.

Correct:
```
missing_evidence:
  - gas_record.json
  - carbon_record.json
acceptance_status: blocked_by_missing_evidence
```
Incorrect:
```
missing_evidence: []
acceptance_status: accepted_bounded_result
```

when files are actually missing.

Evidence Completeness Levels
Level	Meaning
0	No reviewable evidence.
1	Run intent only.
2	Safety preflight plus run intent.
3	Water and power records present.
4	Gas record present but weak or qualitative.
5	Complete baseline bundle with bounded acceptance.
6	Repeat runs or A/B comparison present.
7	Source traceability and carbon accounting present.
8	Calibrated sensors and uncertainty notes present.
9	External review packet present.
10	Standards-aligned validation package present.
Receipt Purpose

The receipt is a concise machine-readable and reviewer-readable summary of the run.

It does not replace raw evidence.

It points to evidence.

Receipt Minimum Fields

```
run_id
branch
objective
preflight_status
run_started
run_completed
water_record_present
power_record_present
gas_record_present
carbon_record_present
thermal_record_present
branch_review_present
hydrogen_specific_detection_present
green_claim_requested
green_claim_supported
advanced_branch_requested
advanced_branch_approved
missing_evidence
anomalies
claim_status
operator_notes
```
Receipt Claim Status Values

Allowed values:
```
no_claim
blocked_by_safety_gate
blocked_by_missing_evidence
blocked_by_advanced_branch_policy
rejected
inconclusive
requires_rerun
accepted_bounded_result
accepted_bounded_phase_management_improvement
accepted_bounded_research_result
```
Forbidden values:
```
proven
validated
certified
commercial_ready
green_hydrogen_confirmed
efficiency_improved
net_positive
safe_for_deployment
```
Acceptance Purpose

Acceptance is the final claim-control decision.

Acceptance answers:

Was the run allowed?
Was the run completed?
Was evidence present?
Was evidence credible?
What bounded claim, if any, can be made?
What claim is forbidden?
What must happen next?
Acceptance Status Values

Use only:
```
accepted_bounded_result
accepted_bounded_phase_management_improvement
accepted_bounded_research_result
rejected
inconclusive
requires_rerun
blocked_by_safety_gate
blocked_by_missing_evidence
blocked_by_missing_baseline
blocked_by_advanced_branch_policy
```
Acceptance Rules: Baseline

Baseline may receive accepted_bounded_result only if:
```
safety_preflight_passed = true
water_record_present = true
power_record_present = true
gas_record_present = true
hydrogen_specific_detection_present = true
leak_check_passed = true
no_pressure_storage = true
no_sealed_accumulation = true
sensor_wetness_corrupted = false
operator_notes_present = true
```

If visible bubbles are the only gas evidence:
```
acceptance_status = rejected
reason = visual_bubbles_only
```
or:
```
acceptance_status = inconclusive
reason = no_hydrogen_specific_detection
```
depending on the record.

Acceptance Rules: Gankyil-A

Gankyil-A may receive accepted_bounded_phase_management_improvement only if:
```
baseline_run_reference_present = true
gankyil_run_record_present = true
comparison_conditions_present = true
conditions_comparable = true
safety_preflight_passed = true
non_pressurized_confirmed = true
sensor_wetness_corrupted = false
phase_management_metric_improved = true
production_claim_requested = false
```
If visual swirl is the only evidence:
```
acceptance_status = rejected
reason = visual_swirl_only
```

Acceptance Rules: Solar Electrical

Solar electrical may support source traceability only if:
```
solar_used = true
source_path_present = true
voltage_v_present = true
current_a_present = true
duration_s_present = true
energy_wh_present = true
carbon_record_present = true
```
If solar hardware is nearby but not connected or measured:
```
green_claim_supported = false
reason = solar_proximity_not_source_traceability
```
Acceptance Rules: Solar Thermal

Solar thermal assist may support a bounded comparison only if:
```
baseline_run_reference_present = true
thermal_assist_used = true
thermal_source_recorded = true
temperature_record_present = true
electrical_input_record_present = true
gas_record_present = true
thermal_input_counted = true
```

If heat is unmeasured:
```
efficiency_claim_supported = false
reason = unmeasured_thermal_input
```

Acceptance Rules: Plasma/Catalyst

Plasma/catalyst branch is blocked unless:
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
If any field is false:
```
acceptance_status = blocked_by_advanced_branch_policy
```
Acceptance Rules: PEC

PEC branch is blocked unless:
```
separate_test_article = true
optical_input_record_method = true
gas_verification_method = true
material_record = true
degradation_tracking = true
safety_preflight = true
```

PEC evidence may not be used to claim baseline electrolysis performance.

Acceptance Rules: Redox

Redox branch is blocked unless:
```
separate_chemistry_review = true
chemical_record_present = true
disposal_plan_present = true
gas_verification_method = true
storage_boundary_defined = true
safety_preflight = true
```
Redox evidence may not be mixed with baseline evidence.

Claim Boundary Layer

The claim boundary converts evidence into allowed and forbidden statements.

Claim Types
Claim Type	Evidence Required
Gas evolution observed	Visual observation only, clearly labeled as non-hydrogen-specific.
Hydrogen detected	Hydrogen-specific detector response.
Hydrogen measured	Calibrated or bounded hydrogen measurement.
Hydrogen output estimated	Hydrogen evidence plus flow/volume method.
Energy input measured	Voltage, current, duration, and energy estimate.
Renewable source traced	Documented solar/battery/source path.
Green-hydrogen bounded claim	Hydrogen evidence plus renewable traceability plus carbon accounting.
Phase-management improvement	Baseline/Gankyil A/B comparison.
Repeatability	Multiple comparable runs.
External review readiness	Complete evidence packet and rejected-run preservation.
Claim Escalation Control

Allowed escalation path:
```
visual gas observation
  -> hydrogen-specific detection
  -> bounded hydrogen measurement
  -> output estimate
  -> repeatable output estimate
  -> renewable-source traceability
  -> carbon-accounted bounded green-H2 claim
  -> external review package
```
Forbidden escalation:
```
visual bubbles
  -> hydrogen proven
  -> green hydrogen proven
  -> efficient system
  -> commercial readiness
```
Green-Hydrogen Claim Gate

A green-hydrogen claim requires:
```
hydrogen_specific_detection_present = true
water_record_present = true
power_record_present = true
energy_source_record_present = true
renewable_fraction_known_or_bounded = true
carbon_record_present = true
safety_preflight_passed = true
acceptance_status in allowed_bounded_statuses
```
If the energy source is unknown:
```
green_claim_supported = false
reason = unknown_energy_source
```
If the battery charge source is unknown:
```
green_claim_supported = false
reason = unknown_battery_charge_source
```

If thermal input is used but unmeasured:
```
efficiency_claim_supported = false
reason = unmeasured_thermal_input
```
Evidence Integrity Rules

The evidence control plane must obey these rules:

Unknown remains unknown.
Missing remains missing.
Failed runs remain preserved.
Blocked runs remain preserved.
Rejected runs remain preserved.
Sensor limitations are recorded.
Wet sensor data is not accepted as clean.
Visual bubbles are not hydrogen proof.
Green claims require source traceability.
Advanced branches require separate review.
Handling Unknown Values

Use:
```
unknown
```
or:
```
not_measured
```
or:
```
not_applicable
```
Do not use:
```
0
```
unless zero was actually measured.

Examples:
renewable_fraction = unknown
hydrogen_concentration_ppm = not_measured
thermal_assist_used = false
thermal_source_temp_c = not_applicable
```
renewable_fraction = unknown
hydrogen_concentration_ppm = not_measured
thermal_assist_used = false
thermal_source_temp_c = not_applicable
```
Handling Failed Runs

Failed runs should produce:
```
run_intent.json
safety_preflight.json
receipt.json
acceptance.json
notes.md
```
Optional but valuable:
```
setup_photos/
anomaly_record.json
maintenance_blocker.json
```
A failed run without complete records is still preserved, but marked as incomplete.

Handling Blocked Runs

Blocked runs should record:
```
run_id
branch
block_reason
preflight_fields_failed
missing_evidence
operator_notes
next_action
```
Examples of block reasons:
```
missing_ventilation
missing_emergency_disconnect
pressure_storage_present
unknown_branch
advanced_branch_policy
missing_hydrogen_sensor
missing_water_record
missing_power_record
```
Handling Inconclusive Runs

Use inconclusive when evidence exists but cannot support a clean result.

Examples:

sensor reading unstable,
sensor calibration unknown,
wetness suspected but not confirmed,
gas path changed during run,
power log partial,
water record incomplete,
comparison conditions not comparable.

Inconclusive is not failure theater.

It is honest uncertainty.

Handling Requires Rerun

Use requires_rerun when the procedure was close but repeat is needed.

Examples:

run completed but one noncritical field was weak,
baseline and Gankyil comparison conditions differed,
operator notes identify a repeatable correction,
sensor warmup was late,
run duration was shorter than intended,
one photo or log was missing but core safety was intact.

Do not use requires_rerun to soften a clear rejection.

Evidence Bundle Review Checklist

A reviewer should be able to answer:

What was the run trying to do?
Which branch was selected?
Was the branch allowed?
Was safety preflight passed?
Was the gas path non-pressurized?
Was water recorded?
Was power recorded?
Was hydrogen detected by a hydrogen-specific method?
Was energy source traceable?
Was carbon accounting possible?
Were there anomalies?
Was the result accepted, rejected, blocked, or inconclusive?
What claim is allowed?
What claim is forbidden?
What is the next action?
Minimum Evidence for First Physical Baseline Claim

Required:
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
Required content:
```
safety_preflight_passed = true
water_record_present = true
power_record_present = true
gas_path_documented = true
hydrogen_specific_detection_present = true
leak_check_passed = true
no_pressure_storage = true
no_sealed_accumulation = true
operator_notes_present = true
```
Allowed claim:
```
GH-BENCH-A0 produced hydrogen-specific detection during a supervised, non-pressurized baseline bench run with recorded water, electrical input, gas-path, safety, and evidence data.
```
Forbidden claim:
```
GH-BENCH-A0 proves green hydrogen.
```
Minimum Evidence for Gankyil-A Claim

Required:
```
baseline_run_reference.json
gankyil_run_reference.json
comparison_conditions.json
phase_management_metrics.json
acceptance.json
notes.md
setup_photos/
```
Allowed claim:
```
Gankyil-A improved one or more practical phase-management metrics under tested GH-BENCH-A0 conditions.
```
Forbidden claim:
```
Gankyil-A improved hydrogen production.
```
Minimum Evidence for Bounded Green-Hydrogen Claim

Required:
```
hydrogen_specific_detection_present = true
water_record_present = true
power_record_present = true
energy_source_record_present = true
renewable_fraction_known_or_bounded = true
carbon_record_present = true
safety_preflight_passed = true
acceptance_status = accepted_bounded_result
```
Allowed claim:
```
A bounded GH-BENCH-A0 run produced hydrogen-specific evidence with documented renewable-energy traceability and carbon-accounting assumptions.
```
Forbidden claim:
```
The system is net-zero, commercial, or fully validated.
```
Control Plane Failure Modes

The evidence control plane fails if it:

accepts a run with missing safety fields,
accepts visual bubbles as hydrogen proof,
accepts unknown energy as renewable,
accepts wet sensor data as clean,
allows plasma branch without review,
hides missing evidence,
deletes failed runs,
inflates claim wording,
treats one run as repeatability,
or allows green-hydrogen claims without carbon accounting.
Control Plane Success Criteria

The evidence control plane succeeds if it:

blocks unsafe runs,
preserves failed runs,
exposes missing evidence,
separates baseline from advanced branches,
ties claims to evidence,
prevents green-hydrogen overclaiming,
supports Gankyil A/B comparison,
produces readable receipts,
produces conservative acceptance results,
and keeps physical proof separate from architecture maturity.
Reviewer Output Summary

Every accepted run should include a reviewer summary like:
```
Run GH-A0-YYYYMMDD-001 was accepted as a bounded baseline result.
The run passed safety preflight, used documented water, recorded electrical input,
used a non-pressurized gas path, recorded hydrogen-specific detection, preserved
operator notes, and generated an evidence receipt.

This run does not prove green hydrogen, efficiency, commercial readiness, or scale-up.
```
Every rejected run should include a reviewer summary like:
```
Run GH-A0-YYYYMMDD-002 was rejected because the hydrogen-specific detection record
was missing. Visible gas bubbles were observed, but visual bubbles are not hydrogen proof.
The run is preserved as a failed evidence artifact.
```
Every blocked run should include a reviewer summary like:
```
Run GH-A0-YYYYMMDD-003 was blocked by the safety gate because ventilation was not
confirmed and the emergency disconnect was not documented. No physical run should proceed.
```

Final Rule

The evidence control plane is the repo's immune system.

Its job is not to make Green-Hydrogen look successful.

Its job is to prevent Green-Hydrogen from lying to itself.



