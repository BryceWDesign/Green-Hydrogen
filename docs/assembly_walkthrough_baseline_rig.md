# Assembly Walkthrough: Non-Pressurized Baseline Rig

## Purpose

This document defines the assembly walkthrough for the first Green-Hydrogen baseline bench rig.

The purpose is not to maximize hydrogen output.

The purpose is to assemble a conservative, non-pressurized, visible, low-output bench setup that can support measured proof-of-concept evidence while blocking unsafe or unsupported claims.

## Rig Name

```
GH-BENCH-A0
```
Assembly Boundary

GH-BENCH-A0 is a validation scaffold.

It is not:

a pressure system,
a hydrogen storage device,
a commercial electrolyzer,
a certified gas appliance,
a field-deployable generator,
an unattended autonomous system,
or a performance-optimized hydrogen system.
Safety Boundary

This walkthrough assumes:

supplier-certified low-output educational or lab electrolysis hardware,
no pressure storage,
no sealed gas accumulation,
no flame testing,
no high-voltage plasma hardware,
no improvised electrolyzer chemistry,
no unattended operation,
no indoor unventilated operation,
and no advanced branch activation during baseline testing.

Physical testing must follow applicable local rules, component documentation, safety guidance, and qualified supervision.

If any selected component requires a different safety procedure, the component documentation overrides this repo.

Assembly Goal

The assembled baseline rig should allow the operator to answer:

What water was used?
What power entered the electrolysis reference module?
What gas path was used?
Was the gas path non-pressurized?
Was hydrogen detected by a hydrogen-specific method?
Was the safety preflight passed?
Was the result accepted, rejected, inconclusive, or blocked?
Can another person understand the setup from the evidence bundle?
Assembly Philosophy

Build for evidence, not output.

The first rig should be:

small,
visible,
stable,
labeled,
non-pressurized,
current-limited,
easy to shut down,
easy to inspect,
easy to disassemble,
and easy to reject if data is weak.
Required Zones

Arrange the bench into six zones.

```
+--------------------------------------------------------------+
| Zone 1: Water Verification                                   |
| - sample containers                                          |
| - pH / TDS / temperature                                     |
| - water record                                               |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Zone 2: Baseline Generation                                  |
| - low-output electrolysis reference module                    |
| - drip tray                                                  |
| - visible water/electrolyte area                             |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Zone 3: Gas-Liquid Handling                                  |
| - simple baseline separator path                             |
| - liquid trap / knock-out trap                               |
| - short visible tubing                                       |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Zone 4: Gas Verification                                     |
| - hydrogen detector / sensor                                 |
| - oxygen-side observation                                    |
| - gas path notes                                             |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Zone 5: Power and Shutdown                                   |
| - current-limited DC supply                                  |
| - inline power meter                                         |
| - fuse / protection                                          |
| - emergency disconnect                                       |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Zone 6: Evidence Capture                                     |
| - laptop/tablet or paper forms                               |
| - run ID labels                                              |
| - camera / photos                                            |
| - evidence folder                                            |
+--------------------------------------------------------------+
```

Zone Separation Rules

Water and electrical zones must not be casually mixed.

Gas verification should be positioned so liquid carryover cannot easily reach the hydrogen sensor.

Power shutdown must be reachable without reaching across the wet zone.

The evidence device should stay outside the splash zone.

The gas path must not terminate near ignition sources.

Step 0: Pre-Assembly Review

Before placing parts on the bench, confirm:

the project is using GH-BENCH-A0 baseline mode,
no advanced branch is active,
no plasma hardware is present,
no pressure storage parts are present,
no flame-test materials are present,
all selected hardware has documentation,
ventilation method is known,
emergency shutdown method is known,
and evidence forms are ready.

If any item fails, stop before assembly.

Step 1: Prepare the Work Area

Place the nonflammable or chemically resistant tray on a stable bench.

Place the splash shield where it protects the operator from liquid splash without creating a sealed gas pocket.

Place absorbent pads only where they do not block airflow, tubing visibility, or emergency access.

Place the first-aid kit, spill kit, and appropriate fire extinguisher nearby according to local guidance.

Post or place visible notes:
```
NO IGNITION SOURCES
NON-PRESSURIZED TEST ONLY
VENTILATION REQUIRED
EMERGENCY DISCONNECT MUST REMAIN REACHABLE
```
Do not continue if the work area is cluttered or if the operator cannot see the full setup.

Step 2: Mark the Six Zones

Use labels or tape to mark:

Water verification.
Baseline generation.
Gas-liquid handling.
Gas verification.
Power and shutdown.
Evidence capture.

The zone layout does not need to be fancy.

It does need to be understandable in photos.

Take a setup photo before installing the gas path.

Save it later as:
```
run_bundles/<run_id>/setup_photos/zone_layout.jpg
```
Step 3: Set Up Water Verification

Place the clean water sample container in Zone 1.

Label it with:

source,
date,
intended run ID,
and operator initials or note.

Prepare the water-record tools:

thermometer,
pH method,
conductivity or TDS method,
measuring container,
water record form.

Do not add electrolyte unless the selected electrolysis reference module requires it and the module documentation is being followed.

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

If the water record is missing, the run may not be accepted.

Step 4: Mount the Baseline Electrolysis Reference Module

Place the low-output electrolysis reference module in Zone 2 inside the drip tray.

Mount or secure it so it cannot tip, slide, or pull on tubing.

Confirm:

it is visible,
it is not sealed,
it is not connected to pressure storage,
it is compatible with the selected water/electrolyte approach,
and it is being used according to its documentation.

Do not modify the electrolysis module for first baseline validation.

Do not chase higher output.

The first job is to confirm the evidence path works.

Step 5: Route the Baseline Gas Path

Connect the electrolysis reference output to the baseline gas-liquid handling path using short, inspectable tubing compatible with the selected hardware.

The baseline path should include:

visible tubing,
a non-pressurized liquid trap or knock-out trap if needed,
a simple gas-liquid separation path,
and a safe vent or verification path.

Label tubing direction with arrows.

Record a simple gas path sketch.

The sketch can be plain text:
```
electrolysis reference module
  -> short visible tube
  -> liquid trap / baseline separator
  -> hydrogen verification point
  -> safe non-pressurized vent path
```
The gas path must not include:

sealed jars,
pressure tanks,
compression hardware,
intentional storage,
blocked outlets,
flame-test ports,
or hidden routing.

If the gas path can trap pressure, reject the layout.

Step 6: Install the Liquid Trap or Baseline Separator

Place the baseline liquid trap or simple separator in Zone 3.

It should be:

visible,
stable,
drainable after shutdown,
non-pressurized,
easy to clean,
and easy to compare against the later Gankyil-A path.

Record:
```
separator_type
separator_orientation
inlet_location
outlet_location
estimated_tubing_length
liquid_trap_present
operator_notes
```
Do not add the Gankyil-A chamber during the first baseline-only assembly unless the run intent specifically says this is a later A/B comparison run.

Step 7: Install Gas Verification Hardware

Place the hydrogen detector or sensor in Zone 4 according to its documentation and safe-use limitations.

Record:

sensor model,
sensor role,
warmup requirement if any,
calibration or bump-test state,
sensor range if known,
sensor placement,
wetness protection method,
and cross-sensitivity notes if known.

If using a separate area hydrogen alarm, place it according to the manufacturer’s instructions and local safety guidance.

If using oxygen-side observation or oxygen sensor hardware, place it so it does not interfere with the non-pressurized gas path.

Do not place sensors where liquid can easily reach them.

If a sensor becomes wet, saturated, unstable, or physically ambiguous, stop and mark the run as rejected or inconclusive.

Step 8: Install the Power and Shutdown Layer

Place the current-limited DC power supply in Zone 5 on the dry side.

Install or confirm:

inline power meter,
fuse or overcurrent protection,
emergency disconnect,
cable labels,
cable strain relief,
and dry routing.

Power must remain off during assembly.

Confirm:
```
emergency_disconnect_reachable = true
wet_zone_crossing_required_for_shutdown = false
fuse_or_protection_present = true
current_limit_recorded = true
power_meter_present = true
```
Reject the layout if shutdown requires reaching across the wet zone.

Reject the layout if cables can be pulled by tubing movement.

Reject the layout if water can drip into connectors.

Step 9: Set Up Evidence Capture

Create the run ID before the run.

Recommended format:
```
GH-A0-YYYYMMDD-001
```

Create the evidence folder:
```
run_bundles/GH-A0-YYYYMMDD-001/
```

Prepare these files or forms:
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
For manual upload or paper logging, prepare equivalent sheets and photograph or transcribe them after the run.

The run is not valid if evidence cannot be stored.

Step 10: Perform Physical Layout Inspection

Before any powered activity, inspect:

water zone stable,
electrolysis module stable,
gas path visible,
separator stable,
tubing direction labeled,
no sealed gas volume,
no pressure storage,
no flame-test path,
hydrogen detector placed,
liquid cannot easily reach sensor,
power supply dry,
emergency disconnect reachable,
ventilation confirmed,
evidence forms ready,
operator stop checklist visible.

If any item fails, do not proceed.

Step 11: Perform Leak and Continuity Review

Perform the leak-check method appropriate for the selected tubing, fittings, and documentation.

The repo does not prescribe a universal leak-check method because the correct method depends on the selected hardware.

Record:
```
leak_check_method
locations_checked
result
operator_notes
```

The run is blocked if:

leak check fails,
leak check is skipped,
gas path is changed after leak check,
or the operator cannot explain the gas path.
Step 12: Run Safety Preflight

Complete the safety preflight before applying power.

Required fields:
```
ventilation_present
no_pressure_storage
no_sealed_accumulation
no_ignition_sources
emergency_disconnect_present
leak_check_passed
water_electric_separation_confirmed
sensors_connected
branch_selected
run_duration_bounded
operator_present
prior_anomalies_resolved
```

Allowed baseline branch:
```
baseline
```

Blocked branches during baseline assembly:
```
plasma_catalyst
solar_thermal_assist
pec
redox
unknown
```

If safety preflight fails, preserve the rejected run record.

Do not “fix it in your head” and continue without updating the record.

Step 13: Baseline Dry Run Without Production Claim

Before a real powered run, perform a dry evidence rehearsal.

This can include:

creating run intent,
completing safety preflight,
checking folder creation,
confirming sensor log fields,
confirming power record fields,
confirming acceptance logic,
and confirming a rejected state is possible.

This dry run should prove the repo can block a bad setup before physical testing.

Step 14: Baseline Powered Run Readiness

Only after the dry run and safety preflight pass may a baseline powered run be considered.

Before applying power, confirm:

operator is present,
PPE is worn,
ventilation is active or confirmed,
no ignition sources are present,
gas path remains non-pressurized,
sensor is ready,
power meter is ready,
timer is ready,
emergency disconnect is reachable,
stop checklist is visible,
and evidence capture is active.

Do not begin if the operator is rushed, uncertain, distracted, or unable to monitor the setup.

Step 15: Start of Baseline Run

At run start, record:
```
start_time
voltage_v
current_a
current_limit_a
water_temperature
hydrogen_sensor_initial_state
oxygen_sensor_initial_state_or_observation
ambient_temperature
ambient_humidity_if_available
operator_notes
```
The initial record matters because later drift can otherwise be misread as production.

Step 16: During-Run Observations

During the run, record observations at defined intervals.

Suggested fields:
```
timestamp
voltage_v
current_a
hydrogen_sensor_reading
oxygen_sensor_reading_or_observation
visible_bubble_behavior
liquid_carryover
sensor_wetness
gas_path_stability
temperature_note
operator_notes
```

Do not change hardware during a run unless stopping for safety.

If hardware changes are needed, stop, record the reason, and start a new run ID after correction.

Step 17: Stop Conditions

Stop immediately if:

ventilation changes,
hydrogen accumulation is suspected,
sensor becomes wet,
tubing disconnects,
liquid reaches verification hardware,
electrical behavior becomes unstable,
unexpected heat occurs,
odor, smoke, spark, or discoloration appears,
gas path becomes blocked,
operator loses line of sight,
data logging fails,
or the operator has any safety concern.

A stopped run is not a failure of the project.

It is a useful evidence artifact.

Step 18: Normal Shutdown

For normal shutdown:

Stop power using the planned shutdown path.
Confirm power is off.
Let the system remain ventilated.
Do not seal any gas path.
Record stop time.
Record final sensor state.
Record final water/gas observations.
Record whether liquid reached the trap or sensor.
Photograph the final setup if safe.
Begin post-run inspection.

Do not disassemble before recording final state unless safety requires immediate disassembly.

Step 19: Post-Run Inspection

After shutdown and ventilation:

Inspect:

tubing,
fittings,
separator,
liquid trap,
electrolysis reference module,
sensor face or inlet,
power leads,
tray,
labels,
and any wet areas.

Record:
```
post_run_leak_observed
liquid_carryover_observed
sensor_wetness_observed
connector_condition
tubing_condition
electrolysis_module_condition
unexpected_residue
operator_notes
```
If sensor wetting occurred, the run should not support a hydrogen claim without review.

Step 20: Evidence Bundle Creation

After the run, assemble:
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

If evidence is manual, transcribe carefully and preserve photos/scans of original sheets.

The evidence bundle must say what is missing.

Do not silently fill missing values.

Step 21: Acceptance Decision

The acceptance result must be one of:
```
accepted_bounded_result
rejected
inconclusive
requires_rerun
blocked_by_safety_gate
blocked_by_missing_evidence
```

A baseline run may be accepted only if it includes:

passed safety preflight,
water record,
power record,
gas path record,
hydrogen-specific detection record,
leak-check record,
non-pressurized confirmation,
operator notes,
and claim boundary.

If any of those are missing, the run should not be accepted.

Step 22: Allowed Baseline Claim

If the baseline run passes, the strongest allowed claim is:
```
GH-BENCH-A0 produced hydrogen-specific detection during a supervised, non-pressurized baseline bench run with recorded water, electrical input, gas-path, safety, and evidence data.
```
This is still not the same as proving green hydrogen.

Step 23: Forbidden Baseline Claims

Do not claim:
```
The system is efficient.
The system is green.
The system is scalable.
The system is commercially ready.
The system is safe for field use.
The system improves hydrogen output.
The Gankyil-A geometry works.
Solar assist improves performance.
Plasma assist improves performance.
```
Those require later evidence.

Step 24: Readiness for Gankyil-A Comparison

The baseline assembly is ready for Gankyil-A comparison only after:

at least one baseline run is accepted or clearly characterized,
the gas path is stable,
the sensor is not being wetted,
the evidence forms work,
the safety gate works,
and the operator can repeat the setup.

Gankyil-A should not be introduced while the baseline setup is still ambiguous.

Assembly Acceptance Checklist

Before declaring the baseline rig assembled:

 Six zones are marked.
 Water verification station is ready.
 Electrolysis reference module is stable.
 Gas path is visible.
 Gas path is non-pressurized.
 No storage volume is present.
 Baseline separator or trap is stable.
 Hydrogen detector is placed and documented.
 Oxygen-side observation is defined.
 Power supply is current-limited.
 Inline power measurement is present.
 Fuse or protection is present.
 Emergency disconnect is reachable.
 Wet and electrical zones are separated.
 Ventilation is confirmed.
 Leak-check method is defined.
 Evidence folder is ready.
 Stop checklist is visible.
 Operator notes are ready.
 No advanced branch is active.
Assembly Rejection Checklist

Reject the assembly if:

 Any pressure storage is present.
 Any sealed gas accumulation path exists.
 Any flame test is planned.
 Ventilation is unknown.
 Emergency disconnect is unreachable.
 Gas path is hidden or unexplained.
 Sensor can be wetted easily.
 Power and water zones are mixed.
 Leak check is skipped.
 Electrolyte is undocumented.
 Sensor model is undocumented.
 Power input cannot be measured.
 Evidence folder is not ready.
 Operator cannot explain stop conditions.
 Plasma, PEC, redox, or thermal assist is active during baseline.
Final Assembly Rule

The first rig is successful when it makes weak evidence obvious.

If the assembled setup makes it easy to overclaim, hide missing data, or ignore safety, it is the wrong setup.

The baseline assembly is not complete until it supports safe rejection as clearly as it supports a bounded accepted result.
