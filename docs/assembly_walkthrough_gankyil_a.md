# Assembly Walkthrough: Gankyil-A Demister / Phase Manager

## Purpose

This document defines the assembly and test pathway for the Gankyil-A passive phase-management chamber.

Gankyil-A is not a hydrogen generator.

Gankyil-A is a removable, non-pressurized gas-liquid handling test article intended to compare practical phase-management behavior against a simpler baseline separator path.

The purpose is to test whether geometry-guided flow can improve:

- gas-liquid separation,
- liquid carryover control,
- sensor wetting reduction,
- condensate behavior,
- gas path stability,
- visual inspectability,
- and repeatability of measurement.

The purpose is not to claim improved hydrogen production without evidence.

## Test Article Name

```
GANKYIL-A
```

Rig Compatibility

GANKYIL-A is designed for use with:
```
GH-BENCH-A0
```

GH-BENCH-A0 must already have a functioning baseline path before GANKYIL-A is tested.

Claim Boundary

Allowed claim after successful A/B evidence:
```
In the GH-BENCH-A0 setup, GANKYIL-A showed improved phase-management behavior compared with the baseline separator path under the tested conditions.
```

Possible supported subclaims, if evidence supports them:
```
GANKYIL-A reduced observed liquid carryover.
GANKYIL-A reduced sensor wetting.
GANKYIL-A improved gas-path stability.
GANKYIL-A made condensate behavior easier to inspect.
GANKYIL-A improved repeatability of gas verification.
```
Forbidden claims:
```
GANKYIL-A increases hydrogen production.
GANKYIL-A improves efficiency.
GANKYIL-A creates energy.
GANKYIL-A proves vortex-enhanced electrolysis.
GANKYIL-A proves green hydrogen.
GANKYIL-A is validated for field use.
```

Those claims require different evidence and are not supported by this test article.

Why Gankyil-A Exists

Early hydrogen bench tests can be corrupted by messy gas-liquid behavior.

Common problems include:

water droplets entering the gas path,
liquid carryover reaching sensors,
bubbles collecting in inconsistent locations,
tubing wetting,
unstable gas readings,
condensate confusing flow estimates,
gas path restrictions,
and difficult-to-repeat separator behavior.

Gankyil-A attempts to make the gas-liquid transition more disciplined and inspectable.

It is a practical demisting and phase-management concept, not an exotic-energy claim.

Design Philosophy

GANKYIL-A should be:

passive,
removable,
inspectable,
non-pressurized,
short-path,
easy to clean,
easy to compare,
and easy to reject if it does not help.

GANKYIL-A should not be:

sealed,
pressurized,
opaque without inspection points,
used for gas storage,
used to increase backpressure,
used with flame testing,
connected to plasma hardware,
or treated as proof by visual swirl alone.
Required Prior Evidence

Do not test GANKYIL-A until the baseline setup has:

Stable non-pressurized gas path.
Working hydrogen-specific detection method.
Water record process.
Electrical input record process.
Safety preflight process.
Leak-check process.
Baseline separator or trap configuration.
Evidence bundle process.
Acceptance decision process.
At least one characterized baseline run.

A bad baseline makes a Gankyil comparison meaningless.

Gankyil-A Role in the System
```
baseline electrolysis reference
  -> gas/liquid output
  -> removable phase-management test article
  -> liquid trap / demist zone
  -> hydrogen verification point
  -> safe non-pressurized vent path
```
GANKYIL-A belongs after gas generation and before final gas verification.

It must not create pressure storage.

Physical Concept

GANKYIL-A is a passive chamber with three conceptual regions:

Inlet region.
Guided swirl / separation region.
Demist / outlet region.
```
+------------------------------------------------+
|                                                |
|  Inlet                                         |
|    v                                           |
|  +----------------------+                      |
|  | Guided separation    |                      |
|  | path / inserts       |                      |
|  +----------------------+                      |
|             |                                  |
|             v                                  |
|  Liquid settles / drains if present            |
|             |                                  |
|             v                                  |
|  Gas exits toward verification path            |
|                                                |
+------------------------------------------------+
```
The exact geometry remains a prototype variable.

The first version should prioritize visibility, safety, and comparison over elegance.

Prototype Geometry Rules

GANKYIL-A should follow these rules:

Chamber must remain non-pressurized.
Chamber must be transparent or inspectable.
Inlet and outlet must be clearly labeled.
Gas outlet must not be blocked.
Liquid trap path must not seal the chamber.
Internal guide features must be removable or cleanable.
Chamber must be mounted in repeatable orientation.
Chamber must be easy to bypass for baseline testing.
Chamber must not require high flow to function.
Chamber must not be treated as storage.
Suggested First Geometry

The first GANKYIL-A prototype should use a simple visible chamber with:

tangential or side-entry inlet if practical,
central or upper gas outlet if practical,
lower liquid collection region,
removable passive guide insert,
visible orientation mark,
external scale marking,
and short tubing connections.

The geometry should not be optimized before the baseline comparison exists.

Orientation

The first test orientation should be vertical or near-vertical unless the chosen chamber design requires another orientation.

Record orientation as:
```
orientation = vertical
orientation_angle_degrees = 90
inlet_position = lower_side
outlet_position = upper_center_or_upper_side
liquid_collection_position = lower_region
```
If using another orientation, document it clearly and photograph it.

Supplier-Neutral Materials

Recommended material classes:

Part	Supplier-Neutral Requirement	Notes
Chamber body	Transparent or inspectable, compatible with water vapor and low-volume hydrogen exposure	Must not be pressure-rated by assumption.
Inlet fitting	Compatible with selected tubing	Must be leak-checked.
Outlet fitting	Compatible with selected tubing	Must not restrict safe venting.
Internal insert	Cleanable, removable, chemically compatible	Should not shed particles.
Mount	Rigid, repeatable, nonconductive preferred	Prevents movement during A/B runs.
Visual scale	External marking only	Do not contaminate interior path.
Drain feature	Optional, non-pressurized only	Must not create sealed accumulation.
Materials Not Allowed

Do not use:

pressure vessels,
glassware not appropriate for the selected use,
improvised sealed containers,
containers with unknown chemical compatibility,
materials that shed particles,
materials that soften under expected conditions,
fittings that force high backpressure,
or opaque housings that prevent inspection.
Step 0: Confirm Baseline Readiness

Before assembling GANKYIL-A, confirm:

GH-BENCH-A0 baseline path exists,
baseline path is non-pressurized,
baseline gas verification works,
safety preflight can pass,
evidence bundle can be created,
leak-check method exists,
no advanced branch is active,
and the operator understands the comparison plan.

If the baseline path is not stable, do not proceed.

Step 1: Define A/B Comparison Plan

Before installing GANKYIL-A, define the comparison.

A-side:
```
A = baseline separator path
```

B-side:
```
B = GANKYIL-A phase-management path
```
Hold constant as much as practical:

water source,
water volume,
electrolyte condition,
electrolysis reference module,
voltage/current range,
run duration,
tubing length where practical,
sensor location,
ambient conditions,
operator procedure,
and evidence forms.

Record anything that differs.

Step 2: Prepare the Chamber Body

Inspect the chamber body.

Confirm:

no cracks,
no residue,
no loose particles,
no sharp internal debris,
inlet/outlet points are clear,
chamber can be cleaned,
chamber can be mounted,
and chamber cannot accidentally seal.

Label:
```
GANKYIL-A
INLET
OUTLET
DRAIN / LIQUID REGION
ORIENTATION MARK
```
If labels cannot be applied safely to the chamber, label the mount or nearby zone instead.

Step 3: Install Internal Guide Insert

If using an internal guide insert, install it before connecting tubing.

The guide insert should:

encourage organized gas-liquid motion,
avoid blocking the outlet,
avoid trapping large pockets,
remain removable,
remain cleanable,
and stay mechanically stable.

The guide insert should not:

scrape or shed particles,
create high restriction,
create sealed compartments,
hide liquid,
or require pressure to function.

Record:
```
guide_insert_present
guide_insert_type
guide_insert_material
guide_insert_removable
guide_insert_cleanable
operator_notes
```
Step 4: Mount GANKYIL-A

Mount GANKYIL-A in Zone 3: Gas-Liquid Handling.

The mount must:

hold the chamber steady,
preserve orientation,
avoid pulling on tubing,
keep the chamber visible,
and allow quick bypass or removal after shutdown.

Do not mount it where:

it blocks emergency access,
it obstructs ventilation,
it hides the gas path,
it sits above unprotected electronics,
or it can tip into the power zone.

Take a photo before tubing is connected.

Step 5: Connect Inlet Tubing

Connect tubing from the baseline electrolysis reference output or upstream trap to the GANKYIL-A inlet.

Use the shortest practical tubing length.

Label flow direction.

Record:
```
inlet_tubing_length
inlet_tubing_material
inlet_fitting_type
inlet_position
inlet_label_confirmed
```
Do not force tubing into a bend that can kink.

Do not create a low point that unintentionally collects liquid unless that is documented.

Step 6: Connect Outlet Tubing

Connect the GANKYIL-A outlet to the hydrogen verification path or downstream trap.

The outlet path must:

remain non-pressurized,
remain visible where practical,
avoid liquid pooling near the sensor,
avoid sharp bends,
and vent safely according to the bench plan.

Record:
```
outlet_tubing_length
outlet_tubing_material
outlet_fitting_type
outlet_position
outlet_label_confirmed
```
The outlet must not be blocked.

Step 7: Confirm Liquid Management

If GANKYIL-A includes a lower liquid collection region or drain feature, confirm that it:

does not create a sealed volume,
does not require pressure to empty,
can be inspected,
can be cleaned after shutdown,
and is not routed toward electronics.

Record:
```
liquid_collection_present
drain_present
drain_state_during_run
liquid_visibility
operator_notes
```
The drain should normally remain configured according to the specific safe test plan.

Do not open or manipulate the drain during an active run unless the run is stopped and made safe.

Step 8: Leak Check

Perform a leak check appropriate to the selected fittings, tubing, and hardware.

Record:
```
leak_check_method
leak_check_locations
leak_check_result
leak_check_notes
```
The run is blocked if:

leak check fails,
leak check is skipped,
any fitting is changed after the leak check,
or the gas path is unclear.
Step 9: Verify Non-Pressurized Path

Before running, confirm:
```
no_pressure_storage = true
no_sealed_accumulation = true
outlet_unblocked = true
vent_path_defined = true
gas_path_visible = true
```
If any field is false, do not run.

Step 10: Sensor Wetness Protection

Confirm that the GANKYIL-A outlet does not send liquid directly into the hydrogen sensor.

Preferred order:
```
GANKYIL-A
  -> optional downstream liquid trap / demist buffer
  -> hydrogen verification point
  -> safe vent path
```
Record:
```
sensor_wetness_protection_present
downstream_trap_present
sensor_position
operator_notes
```
If liquid reaches the sensor during testing, stop and mark the run as rejected or inconclusive.

Step 11: GANKYIL-A Preflight

Complete a preflight specific to the GANKYIL-A comparison.

Required fields:
```
baseline_run_reference
gankyil_chamber_installed
gankyil_orientation_recorded
inlet_outlet_labeled
guide_insert_recorded
non_pressurized_confirmed
leak_check_passed
sensor_wetness_protection_confirmed
evidence_forms_ready
operator_present
```

If any required field is missing, the Gankyil run is blocked.

Step 12: Run the Baseline A-Side

Before the B-side test, run or reference the A-side baseline separator test.

The A-side record must include:
```
run_id
separator_type = baseline
water_source
power_input
run_duration
hydrogen_detection
liquid_carryover_observation
sensor_wetness_observation
gas_path_stability
condensate_behavior
operator_notes
```

If no A-side record exists, do not claim B-side improvement.

Step 13: Run the Gankyil B-Side

For the B-side run, keep the setup as close as practical to the A-side.

Record:
```
run_id
separator_type = gankyil_a
water_source
power_input
run_duration
hydrogen_detection
liquid_carryover_observation
sensor_wetness_observation
gas_path_stability
condensate_behavior
operator_notes
```

Do not change power, water, sensor position, or run duration casually.

If anything changes, record it.

Step 14: During-Run Observations

During the Gankyil run, observe:

visible bubble path,
liquid carryover,
liquid collection,
sensor wetness,
gas path stability,
tubing vibration or pulsing,
condensate behavior,
signs of restriction,
unexpected heating,
and sensor reading stability.

Suggested interval log:
```
timestamp
voltage_v
current_a
hydrogen_sensor_reading
visible_bubble_behavior
liquid_carryover
sensor_wetness
gankyil_chamber_liquid_level
gas_path_stability
restriction_concern
operator_notes
```
Step 15: Stop Conditions

Stop the Gankyil run if:

liquid reaches the sensor,
outlet appears restricted,
pressure buildup is suspected,
tubing disconnects,
chamber leaks,
guide insert shifts,
ventilation changes,
gas path becomes unclear,
sensor readings become unstable,
electrical behavior changes unexpectedly,
or the operator has any safety concern.

A stopped run is still useful evidence.

Step 16: Normal Shutdown

For normal shutdown:

Stop power.
Confirm power is off.
Maintain ventilation.
Do not seal gas path.
Record final sensor readings.
Photograph final chamber state if safe.
Record liquid level and carryover.
Wait until safe before disassembly or drain handling.
Complete post-run notes.
Preserve evidence.
Step 17: Post-Run Inspection

After shutdown, inspect:

inlet fitting,
outlet fitting,
chamber body,
guide insert,
liquid collection region,
tubing,
downstream trap,
hydrogen sensor inlet or face,
and mount stability.

Record:
```
post_run_leak_observed
liquid_carryover_observed
sensor_wetness_observed
guide_insert_shifted
residue_observed
cleaning_required
operator_notes
```
If the guide insert moved or the chamber restricted flow, the run should not support an improvement claim without review.

Step 18: Cleaning and Reset

After testing and safe shutdown:

disconnect only after gas path is safe,
drain liquid according to the selected safe procedure,
clean chamber using a compatible method,
dry parts before storage,
inspect for residue or damage,
remove labels only if replacing them,
and store parts in a marked container.

Record:
```
cleaning_method
chamber_condition_after_cleaning
insert_condition_after_cleaning
ready_for_reuse
maintenance_notes
```
Do not reuse a damaged chamber.

Step 19: A/B Evidence Bundle

A complete A/B comparison should include:
```
run_bundles/<comparison_id>/
  baseline_run_reference.json
  gankyil_run_reference.json
  comparison_conditions.json
  gankyil_installation_record.json
  liquid_carryover_observations.json
  sensor_wetness_observations.json
  gas_path_stability_notes.md
  setup_photos/
  acceptance.json
```
If the comparison uses separate run folders, the comparison bundle should reference both run IDs.

Step 20: Comparison Metrics

Compare A-side and B-side on practical metrics:

Metric	Baseline A	Gankyil B	Better / Worse / Same / Unknown
Liquid carryover			
Sensor wetting			
Gas path stability			
Visible bubble organization			
Condensate behavior			
Cleaning burden			
Setup complexity			
Repeatability			
Safety concerns			
Measurement clarity			

Do not score Gankyil-A as better merely because it looks more complex.

Step 21: Acceptance Decision

Allowed acceptance statuses:
```
accepted_bounded_phase_management_improvement
rejected
inconclusive
requires_rerun
blocked_by_safety_gate
blocked_by_missing_baseline
blocked_by_missing_evidence
```
A Gankyil improvement claim requires:

valid A-side baseline record,
valid B-side Gankyil record,
comparable conditions,
no safety block,
no wet sensor corruption,
gas path record,
and documented improvement in at least one phase-management metric.
Step 22: Strongest Allowed Gankyil Claim

If evidence supports it, the strongest allowed claim is:
```
Under GH-BENCH-A0 test conditions, GANKYIL-A improved one or more practical phase-management metrics compared with the baseline separator path.
```
That is still not a hydrogen-output claim.

Step 23: Forbidden Gankyil Claims

Do not claim:
```
GANKYIL-A increases hydrogen production.
GANKYIL-A improves electrolysis efficiency.
GANKYIL-A creates energy.
GANKYIL-A proves vortex hydrogen.
GANKYIL-A proves green hydrogen.
GANKYIL-A is validated for scale-up.
```
Those require separate evidence not generated by this comparison.

Assembly Acceptance Checklist

Before running GANKYIL-A:

 Baseline path has already been characterized.
 A/B comparison plan exists.
 GANKYIL-A chamber is visible or inspectable.
 Chamber is non-pressurized.
 Inlet is labeled.
 Outlet is labeled.
 Outlet is unblocked.
 Guide insert is recorded.
 Orientation is recorded.
 Chamber is mounted securely.
 Tubing is short and labeled.
 Sensor wetness protection exists.
 Leak check passed.
 Vent path is defined.
 Evidence forms are ready.
 Operator is present.
 Stop conditions are visible.
 No advanced branch is active.
Assembly Rejection Checklist

Reject the GANKYIL-A setup if:

 Baseline comparison is missing.
 Gas path can become pressurized.
 Outlet can be blocked.
 Chamber is opaque and uninspectable.
 Liquid can directly reach the hydrogen sensor.
 Guide insert can shift freely.
 Chamber leaks.
 Tubing is kinked.
 Vent path is unclear.
 Evidence forms are missing.
 Plasma/catalyst branch is active.
 Operator cannot explain the gas path.
 The setup relies on visual swirl as proof.
Design Iteration Rules

Future Gankyil-A variants should be named:
```
GANKYIL-A1
GANKYIL-A2
GANKYIL-A3
```
Do not overwrite prior results.

Each variant should record:
```
variant_id
geometry_change
reason_for_change
expected_effect
test_conditions
result
accepted_or_rejected
notes
```
What Would Make Gankyil-A Worth Keeping

GANKYIL-A earns its place only if it improves at least one practical validation metric without making the system less safe or harder to measure.

Useful improvements include:

fewer wet sensor events,
less liquid carryover,
easier condensate observation,
more stable readings,
easier repeat setup,
clearer gas path photos,
easier post-run cleaning,
or better repeatability.
What Would Make Gankyil-A Worth Removing

Remove or redesign GANKYIL-A if it:

increases restriction,
causes sensor wetting,
hides liquid,
complicates evidence,
adds leak points,
becomes hard to clean,
creates ambiguous gas behavior,
or encourages unsupported claims.
Final Rule

GANKYIL-A is allowed to be interesting.

It is not allowed to be mystical.

It earns credibility only through side-by-side evidence against the baseline path.
