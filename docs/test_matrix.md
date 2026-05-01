# Test Matrix

## Purpose

This document defines the Green-Hydrogen test matrix.

The test matrix exists to keep validation structured, safe, repeatable, and honest.

The goal is not to prove the system by force.

The goal is to create a disciplined sequence that can produce one of four honest outcomes:

1. Accepted bounded result.
2. Rejected result.
3. Inconclusive result.
4. Blocked run.

All four outcomes are valid engineering outputs.

## Target Platform

```
GH-BENCH-A0
```

Primary Validation Questions

The test matrix is built around these questions:

Can the repo block unsafe or incomplete run intents?
Can the first rig be assembled as a non-pressurized baseline system?
Can water input be documented before testing?
Can electrical input be measured?
Can hydrogen-specific detection be recorded?
Can gas path behavior be documented?
Can failed and rejected runs be preserved?
Can Gankyil-A be compared against a baseline separator?
Can solar electrical input be traced?
Can solar thermal assist be tested without hiding thermal energy?
Can carbon accounting prevent false green-hydrogen claims?
Can advanced branches remain blocked until review?
Test Matrix Summary
Test ID	Test Name	Level	Branch	Status	Purpose
T-000	Repo structure smoke test	0	none	Required	Confirm repo can run basic checks.
T-001	Dry run: valid baseline intent	1	baseline	Required	Confirm baseline run intent passes dry validation.
T-002	Dry run: missing evidence blocked	1	baseline	Required	Confirm missing evidence blocks acceptance.
T-003	Dry run: plasma branch blocked	1	plasma_catalyst	Required	Confirm advanced branch is denied by default.
T-004	Dry run: unknown branch blocked	1	unknown	Required	Confirm undefined branch is denied.
T-005	Assembly inspection: six-zone layout	2	baseline	Required	Confirm physical layout is understandable.
T-006	Assembly inspection: non-pressurized gas path	2	baseline	Required	Confirm no pressure storage or sealed accumulation.
T-007	Assembly inspection: emergency disconnect	2	baseline	Required	Confirm shutdown can occur without crossing wet zone.
T-008	Water verification record	2	baseline	Required	Confirm water evidence exists before run.
T-009	Power measurement record	2	baseline	Required	Confirm voltage/current/duration are captured.
T-010	Gas verification rack readiness	2	baseline	Required	Confirm sensor, leak-check, and vent path are ready.
T-011	Baseline hydrogen detection run	3	baseline	Required	First bounded hydrogen-specific detection attempt.
T-012	Baseline repeat run 1	5	baseline	Required later	Confirm repeatability begins.
T-013	Baseline repeat run 2	5	baseline	Required later	Confirm repeatability set.
T-014	Calibrated hydrogen measurement	4	baseline	Required later	Upgrade detection confidence.
T-015	Flow or volume estimate	4	baseline	Optional later	Add output estimate without pressure storage.
T-016	Oxygen-side observation	4	baseline	Required for stronger evidence	Record oxygen-side behavior or crossover concern.
T-017	Gankyil-A install inspection	6	gankyil_a	Required before A/B	Confirm safe removable phase manager.
T-018	Gankyil-A A/B comparison	6	gankyil_a	Required later	Compare phase-management behavior.
T-019	Gankyil-A repeat comparison	6	gankyil_a	Optional later	Test repeatability of phase-management improvement.
T-020	Solar electrical traceability dry run	7	solar_electrical	Optional later	Confirm source record structure.
T-021	Solar electrical powered comparison	7	solar_electrical	Optional later	Test solar-traceable electrical input.
T-022	Solar thermal assist dry review	8	solar_thermal_assist	Optional later	Confirm thermal evidence fields.
T-023	Solar thermal assist comparison	8	solar_thermal_assist	Optional later	Compare baseline and thermal-assisted run.
T-024	Carbon accounting check	9	baseline/solar	Required	Confirm green claim is blocked or bounded correctly.
T-025	External review packet dry assembly	10	none	Optional later	Confirm reviewer package completeness.
T-026	Failed-run preservation test	1-10	any	Required	Confirm failed run remains documented.
T-027	Maintenance blocker test	2	any	Required	Confirm unresolved hardware issue blocks run.
T-028	Sensor wetness rejection test	3-6	baseline/gankyil	Required later	Confirm wet sensor prevents accepted claim.
T-029	Unknown source rejection test	9	baseline/solar	Required	Confirm unknown energy source blocks green claim.
T-030	Advanced branch review gate	10	advanced	Future only	Confirm plasma/PEC/redox require separate review.
Test Status Definitions
Status	Meaning
Required	Needed for the main validation path.
Required later	Needed after baseline setup is stable.
Optional later	Useful but not part of first proof.
Future only	Not allowed in first baseline stage.
Blocked	Must not run until prerequisites are satisfied.
Complete	Test has evidence bundle and acceptance result.
Acceptance Status Values

Every test must end with one of these statuses:
```
accepted_bounded_result
accepted_bounded_phase_management_improvement
rejected
inconclusive
requires_rerun
blocked_by_safety_gate
blocked_by_missing_evidence
blocked_by_missing_baseline
blocked_by_advanced_branch_policy
```
Required Evidence Files

For a physical baseline run:
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

For a Gankyil-A A/B comparison:
```
baseline_run_reference.json
gankyil_run_reference.json
comparison_conditions.json
phase_management_metrics.json
acceptance.json
notes.md
setup_photos/
```
For solar or thermal runs:
```
energy_source_record.json
thermal_record.json
carbon_record.json
acceptance.json
notes.md
```
T-000: Repo Structure Smoke Test
Purpose

Confirm that the repo has a working minimum structure and the code scaffold can be imported or tested.

Type

Dry software test.

Prerequisites
Python package scaffold exists.
Tests folder exists.
Example files exist.
Inputs
```
src/green_hydrogen/
tests/
examples/
docs/
```
Procedure
Confirm package imports.
Confirm smoke test runs.
Confirm example run intent can be read.
Confirm safety preflight can return an allow or deny result.
Confirm acceptance logic can reject missing evidence.
Acceptance Criteria

Accept if:

package imports,
tests execute,
no required scaffold file is missing,
and example blocked runs remain blocked.
Rejection Criteria

Reject if:

package cannot import,
safety gate cannot run,
acceptance logic fails open,
or missing evidence is silently accepted.

Allowed Claim
```
The repo scaffold passes dry smoke testing.
```
Forbidden Claim
```
The physical system is validated.
```
T-001: Dry Run: Valid Baseline Intent
Purpose

Confirm that a well-formed baseline run intent can pass dry preflight when safety fields are true.

Type

Dry software/evidence test.

Inputs
```
examples/baseline_pem_1g_hr_run_intent.json
```
Procedure
Load baseline run intent.
Confirm branch is baseline.
Confirm run duration is bounded.
Confirm preflight fields are present.
Run safety preflight.
Generate receipt.
Generate acceptance decision.
Acceptance Criteria

Accept if:

baseline branch is recognized,
no advanced branch is requested,
safety preflight passes in dry form,
and acceptance remains bounded.
Rejection Criteria

Reject if:

branch is unknown,
safety field is missing,
pressure storage appears,
or acceptance produces an inflated claim.

Allowed Claim
```
The dry baseline run intent is structurally valid.
```
T-002: Dry Run: Missing Evidence Blocked
Purpose

Confirm that a run with missing evidence cannot be accepted.

Type

Dry software/evidence test.

Inputs
```
examples/rejected_missing_evidence_bundle.json
```

Procedure
Load rejected evidence bundle.
Confirm required fields are missing.
Run receipt generation.
Run acceptance logic.
Confirm result is blocked or rejected.
Acceptance Criteria

Accept this test if the bad run is rejected.

Rejection Criteria

Reject this test if the bad run is accepted.

Allowed Claim
```
The acceptance layer blocks missing evidence in dry-run form.
```

T-003: Dry Run: Plasma Branch Blocked
Purpose

Confirm that plasma/catalyst activation is blocked by default.

Type

Dry policy test.

Inputs
```
examples/plasma_assist_blocked_review_required.json
```
Procedure
Load plasma branch run intent.
Confirm branch is plasma_catalyst.
Run safety preflight.
Confirm branch is denied.
Confirm receipt records review requirement.
Acceptance Criteria

Accept if:

preflight denies the run,
branch status is blocked,
and no accepted result is possible.
Rejection Criteria

Reject if plasma/catalyst branch can run without review.

Allowed Claim
```
The plasma/catalyst branch is blocked by default.
```

T-004: Dry Run: Unknown Branch Blocked
Purpose

Confirm that unknown branch labels do not pass the policy gate.

Type

Dry policy test.

Inputs

Any run intent with:
```
branch = unknown
```
Acceptance Criteria

Accept if unknown branch is blocked.

Rejection Criteria

Reject if unknown branch is allowed.

Safety Note

Unknown branch must never fail open.

T-005: Assembly Inspection: Six-Zone Layout
Purpose

Confirm that the physical bench layout is clear.

Type

Physical inspection.

Prerequisites
No power applied.
No gas production.
Bench components placed.
Required Zones
```
Zone 1: Water verification
Zone 2: Baseline generation
Zone 3: Gas-liquid handling
Zone 4: Gas verification
Zone 5: Power and shutdown
Zone 6: Evidence capture
```
Evidence
setup photo,
zone labels,
operator notes.
Acceptance Criteria

Accept if:

six zones are visible or clearly described,
wet and dry zones are separated,
emergency access is not blocked,
and evidence capture is outside splash zone.
Rejection Criteria

Reject if:

zones are unclear,
power and wet zones are mixed,
operator cannot explain the layout,
or emergency disconnect is blocked.
T-006: Assembly Inspection: Non-Pressurized Gas Path
Purpose

Confirm the gas path cannot intentionally store or pressurize hydrogen.

Type

Physical inspection.

Evidence
```
gas_path_sketch
tubing_direction_labels
vent_path_record
no_pressure_storage_confirmation
no_sealed_accumulation_confirmation
```
Acceptance Criteria

Accept if:

gas path is visible where practical,
outlet is unblocked,
no storage tank exists,
no sealed collection exists,
and vent path is defined.
Rejection Criteria

Reject if:

any sealed volume exists,
outlet can be blocked,
pressure storage exists,
vent path is unclear,
or operator cannot explain the gas path.
T-007: Assembly Inspection: Emergency Disconnect
Purpose

Confirm that power can be stopped quickly and safely.

Type

Physical inspection.

Evidence
```
emergency_disconnect_photo
emergency_disconnect_location
operator_reachability_note
wet_zone_crossing_required_for_shutdown
```
Acceptance Criteria

Accept if:

emergency disconnect exists,
it is labeled,
it is reachable from operator position,
and operator does not need to cross wet zone to use it.
Rejection Criteria

Reject if:

disconnect is missing,
disconnect is blocked,
disconnect requires reaching over gas/water hardware,
or operator cannot identify it instantly.
T-008: Water Verification Record
Purpose

Confirm input water is documented before run.

Type

Physical/evidence test.

Evidence Fields
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
Acceptance Criteria

Accept if required water fields are completed or honestly marked unknown where allowed.

Rejection Criteria

Reject accepted-run status if water record is missing.

Claim Rule

Unknown water blocks strong interpretation.

T-009: Power Measurement Record
Purpose

Confirm electrical input can be recorded.

Type

Physical/evidence test.

Evidence Fields
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
Acceptance Criteria

Accept if voltage, current, duration, and source are recorded.

Rejection Criteria

Reject energy or efficiency claims if power record is missing or incomplete.

T-010: Gas Verification Rack Readiness
Purpose

Confirm the gas verification rack is ready before a live run.

Type

Physical inspection.

Evidence Fields
```
incoming_path_labeled
liquid_protection_present
hydrogen_sensor_installed
hydrogen_sensor_recorded
sensor_wetness_protection_confirmed
optional_flow_method_safe
oxygen_side_record_defined
vent_path_defined
ventilation_confirmed
no_storage_confirmed
leak_check_passed
evidence_forms_ready
operator_present
```
Acceptance Criteria

Accept if all required fields pass.

Rejection Criteria

Reject if:

hydrogen sensor is missing,
leak check fails,
vent path is undefined,
liquid can reach sensor easily,
or gas path can become pressurized.
T-011: Baseline Hydrogen Detection Run
Purpose

Attempt the first bounded hydrogen-specific detection using the baseline configuration.

Type

Physical validation test.

Prerequisites
T-005 through T-010 accepted.
Safety preflight passed.
Evidence folder created.
No advanced branch active.
Procedure
Create run intent.
Complete safety preflight.
Record water evidence.
Record power starting state.
Record gas verification starting state.
Apply power within selected module documentation and current limit.
Record sensor and power observations at intervals.
Stop normally or by stop condition.
Record post-run inspection.
Generate receipt.
Generate acceptance result.
Acceptance Criteria

Accept only if:

safety preflight passed,
water record exists,
power record exists,
gas path record exists,
hydrogen-specific detection exists,
leak check passed,
no pressure storage exists,
no sensor wetness corrupted the result,
and evidence bundle is complete enough to review.
Rejection Criteria

Reject if:

visual bubbles are the only gas evidence,
sensor is wet,
power record is missing,
water record is missing,
leak check fails,
gas path is unknown,
or ventilation is missing.

Allowed Claim
```
The GH-BENCH-A0 baseline configuration produced hydrogen-specific detection under documented, non-pressurized bench conditions.
```
Forbidden Claim
```
The system produces green hydrogen efficiently.
```

T-012: Baseline Repeat Run 1
Purpose

Begin repeatability testing after first accepted or characterized baseline run.

Prerequisites
T-011 complete.
Baseline setup unchanged or changes documented.
Acceptance Criteria

Accept if repeat run uses comparable conditions and produces reviewable evidence.

Rejection Criteria

Reject repeatability claim if conditions changed and were not documented.

T-013: Baseline Repeat Run 2
Purpose

Complete a three-run baseline set when combined with T-011 and T-012.

Prerequisites
T-011 complete.
T-012 complete.
Acceptance Criteria

Accept if three comparable baseline runs exist.

Rejection Criteria

Reject repeatability claim if fewer than three comparable runs exist.

T-014: Calibrated Hydrogen Measurement
Purpose

Upgrade hydrogen evidence from detection to bounded measurement.

Prerequisites
Hydrogen sensor model selected.
Calibration or bump-test state recorded.
Baseline gas path stable.
Evidence Fields
```
hydrogen_sensor_model
sensor_range
calibration_state
bump_test_state
sensor_position
sensor_limitations
hydrogen_reading
uncertainty_note
```
Acceptance Criteria

Accept if sensor state supports the claimed evidence level.

Rejection Criteria

Reject quantitative claim if sensor is uncalibrated, saturated, wet, or outside known range.

T-015: Flow or Volume Estimate
Purpose

Add bounded output estimate without creating pressure risk.

Prerequisites
Baseline hydrogen detection works.
Flow or volume method reviewed.
No pressure buildup risk.
Acceptance Criteria

Accept if measurement method does not restrict gas path and is documented.

Rejection Criteria

Reject if flow device creates backpressure, traps gas, or corrupts sensor path.

T-016: Oxygen-Side Observation
Purpose

Record oxygen-side behavior or crossover concern.

Evidence Fields
```
oxygen_observation_present
oxygen_sensor_model_or_method
oxygen_side_behavior
crossover_concern
operator_notes
```
Acceptance Criteria

Accept if oxygen-side condition is documented.

Rejection Criteria

Reject or mark inconclusive if crossover is suspected.

T-017: Gankyil-A Install Inspection
Purpose

Confirm Gankyil-A is safely installed before A/B comparison.

Prerequisites
Baseline setup characterized.
Gankyil-A chamber assembled.
No advanced branch active.
Evidence Fields
```
gankyil_chamber_installed
gankyil_orientation_recorded
inlet_outlet_labeled
guide_insert_recorded
non_pressurized_confirmed
leak_check_passed
sensor_wetness_protection_confirmed
operator_present
```
Acceptance Criteria

Accept if chamber is removable, non-pressurized, leak-checked, and documented.

Rejection Criteria

Reject if outlet can be blocked, chamber leaks, sensor wetness risk is high, or baseline comparison is missing.

T-018: Gankyil-A A/B Comparison
Purpose

Compare Gankyil-A phase-management behavior against baseline separator path.

Prerequisites
Valid baseline A-side record.
Gankyil-A install inspection accepted.
Comparable conditions defined.
Metrics
```
liquid_carryover
sensor_wetting
gas_path_stability
visible_bubble_organization
condensate_behavior
cleaning_burden
setup_complexity
repeatability
safety_concerns
measurement_clarity
```
Acceptance Criteria

Accept bounded phase-management improvement if:

A-side and B-side records exist,
conditions are comparable,
no safety block occurred,
evidence shows improvement in at least one practical phase-management metric,
and no forbidden production claim is made.
Rejection Criteria

Reject if:

no baseline comparison exists,
Gankyil path restricts flow,
sensor is wetted,
comparison conditions are unclear,
or result is based only on visual swirl.

Allowed Claim
```
Gankyil-A improved one or more practical phase-management metrics under tested GH-BENCH-A0 conditions.
```
T-019: Gankyil-A Repeat Comparison
Purpose

Confirm whether Gankyil-A improvement repeats.

Prerequisites
T-018 complete.
Same or documented revised Gankyil variant.
Acceptance Criteria

Accept repeatability only if at least two comparable A/B comparisons exist.

Rejection Criteria

Reject repeatability claim if only one A/B comparison exists.

T-020: Solar Electrical Traceability Dry Run
Purpose

Confirm solar source evidence fields work before solar powered testing.

Type

Dry evidence test.

Evidence Fields
```
solar_used
panel_description
source_path
voltage_v
current_a
duration_s
battery_used
battery_charge_source
weather_note
renewable_fraction
```
Acceptance Criteria

Accept if dry record supports source traceability.

Rejection Criteria

Reject if source is vague or battery charge source is unknown but claimed renewable.

T-021: Solar Electrical Powered Comparison
Purpose

Test solar-traceable electrical input after stable baseline evidence.

Prerequisites
Baseline evidence exists.
Solar path measured.
Emergency shutdown remains available.
Acceptance Criteria

Accept bounded solar electrical run if source path and electrical input are documented.

Rejection Criteria

Reject green claim if solar input is not measured or source path is incomplete.

T-022: Solar Thermal Assist Dry Review
Purpose

Confirm thermal assist evidence fields before any thermal test.

Type

Dry evidence/safety review.

Evidence Fields
```
thermal_assist_used
thermal_source
thermal_source_temp
water_temp_start
water_temp_end
cell_surface_temp
exposure_duration
contact_method
sensor_drift_concern
thermal_anomaly
```
Acceptance Criteria

Accept dry readiness if thermal input can be measured and counted.

Rejection Criteria

Reject thermal test if thermal input would be unmeasured or hidden.

T-023: Solar Thermal Assist Comparison
Purpose

Compare baseline and thermal-assisted condition.

Prerequisites
Stable baseline.
Thermal dry review accepted.
Temperature monitoring available.
Acceptance Criteria

Accept only as bounded comparison if thermal and electrical inputs are both recorded.

Rejection Criteria

Reject efficiency claim if thermal input is not counted.

T-024: Carbon Accounting Check
Purpose

Confirm carbon accounting blocks unsupported green-hydrogen claims.

Type

Evidence/software test.

Inputs
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
```
Acceptance Criteria

Accept if carbon module marks unknowns honestly and blocks unsupported green claim.

Rejection Criteria

Reject if unknown source is treated as renewable or zero-carbon.

T-025: External Review Packet Dry Assembly
Purpose

Prepare a reviewable packet from repo docs and run bundles.

Required Contents
```
architecture_summary
BOM
assembly_walkthrough
safety_policy
hazard_register
validation_plan
test_matrix
raw_run_evidence
rejected_runs
accepted_runs
calibration_records
photos
claim_boundary_statement
reviewer_checklist
```
Acceptance Criteria

Accept if a reviewer can understand what was tested, what failed, what passed, and what is not claimed.

Rejection Criteria

Reject if the packet hides failed runs, lacks raw evidence, or overstates claims.

T-026: Failed-Run Preservation Test
Purpose

Confirm rejected and blocked runs are preserved.

Procedure
Create or load bad run.
Run safety or acceptance logic.
Confirm rejected status.
Confirm receipt preserves reason.
Confirm result is not deleted.
Acceptance Criteria

Accept if failed run remains reviewable.

Rejection Criteria

Reject if failed run is overwritten, deleted, or converted to success.

T-027: Maintenance Blocker Test
Purpose

Confirm unresolved hardware issue blocks testing.

Example Blockers
```
damaged_tubing
wet_sensor
expired_sensor_state
missing_fuse
leaking_fitting
cracked_chamber
unresolved_prior_anomaly
```
Acceptance Criteria

Accept if blocker prevents run.

Rejection Criteria

Reject if run proceeds with unresolved blocker.

T-028: Sensor Wetness Rejection Test
Purpose

Confirm wet hydrogen sensor blocks accepted hydrogen claim.

Type

Physical/evidence rejection test.

Acceptance Criteria

Accept this test if wet sensor causes rejection or inconclusive result.

Rejection Criteria

Reject this test if wet sensor data is accepted as clean hydrogen evidence.

T-029: Unknown Source Rejection Test
Purpose

Confirm unknown energy source blocks green-hydrogen claim.

Inputs
```
source_type = unknown
renewable_fraction = unknown
```
Acceptance Criteria

Accept if green claim is blocked.

Rejection Criteria

Reject if unknown source is treated as green.

T-030: Advanced Branch Review Gate
Purpose

Confirm advanced branches cannot run without separate review.

Advanced Branches
```
plasma_catalyst
pec
redox
high_temperature_thermal
unknown_catalyst
```
Acceptance Criteria

Accept if all advanced branches are blocked by default.

Rejection Criteria

Reject if any advanced branch can run through baseline pathway.

Test Execution Order

Recommended order:
```
T-000
T-001
T-002
T-003
T-004
T-005
T-006
T-007
T-008
T-009
T-010
T-011
T-012
T-013
T-014
T-015
T-016
T-017
T-018
T-019
T-020
T-021
T-022
T-023
T-024
T-025
T-026
T-027
T-028
T-029
T-030
```
Do not run optional physical tests before required baseline tests are stable.

Minimum First Proof Package

The first useful proof package includes:
```
T-000 repo smoke test
T-001 valid baseline dry run
T-002 missing evidence blocked
T-003 plasma branch blocked
T-005 six-zone layout
T-006 non-pressurized gas path
T-007 emergency disconnect
T-008 water verification
T-009 power measurement
T-010 gas verification rack readiness
T-011 baseline hydrogen detection run
T-024 carbon accounting check
T-026 failed-run preservation
```
Minimum Gankyil-A Package

The first useful Gankyil-A package includes:
```
accepted or characterized baseline run
T-017 Gankyil-A install inspection
T-018 Gankyil-A A/B comparison
T-026 failed-run preservation
T-028 sensor wetness rejection
```
Minimum Green-Hydrogen Claim Package

A bounded green-hydrogen claim requires:
```
hydrogen-specific evidence
water evidence
power evidence
energy source traceability
renewable fraction estimate
carbon accounting note
safety preflight
leak check
non-pressurized confirmation
acceptance decision
claim boundary
```
If any item is missing, the green-hydrogen claim is blocked.

Test Matrix Maintenance

Update the test matrix when:

exact hardware is selected,
sensor model changes,
Gankyil geometry changes,
validation level changes,
a hazard is added,
an anomaly occurs,
a test fails,
or an external reviewer identifies a missing test.
Final Rule

A test matrix is useful only if it can say no.

If every test is designed to pass, the matrix is theater.

Green-Hydrogen testing must be able to reject the project’s favorite assumptions.
