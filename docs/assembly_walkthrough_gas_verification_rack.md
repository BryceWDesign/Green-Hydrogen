# Assembly Walkthrough: Gas Verification Rack

## Purpose

This document defines the assembly walkthrough for the Green-Hydrogen gas verification rack.

The gas verification rack is the measurement zone that sits downstream of the baseline separator or Gankyil-A phase-management chamber.

Its job is not to store hydrogen.

Its job is to make hydrogen evidence harder to fake, easier to review, and safer to reject when the data is weak.

## Rack Name

```
GH-GASVERIFY-A0
```
Scope

GH-GASVERIFY-A0 includes:

Non-pressurized gas verification path.
Hydrogen-specific detection method.
Optional oxygen-side observation or sensor.
Liquid carryover protection.
Leak-check discipline.
Sensor position record.
Gas path sketch.
Evidence record.
Acceptance support.

GH-GASVERIFY-A0 excludes:

Hydrogen storage.
Compression.
Flame tests.
Pressurized sampling.
Sealed gas accumulation.
Unvented collection.
High-temperature ignition checks.
Any claim of purity without proper measurement.
Claim Boundary

Allowed bounded claim after successful evidence:
```
GH-GASVERIFY-A0 recorded hydrogen-specific detection in a non-pressurized bench gas path with documented water, power, safety, and gas-path evidence.
```

Forbidden claims:
```
GH-GASVERIFY-A0 proves high-purity hydrogen.
GH-GASVERIFY-A0 proves green hydrogen.
GH-GASVERIFY-A0 proves efficient hydrogen production.
GH-GASVERIFY-A0 is a certified gas-analysis system.
GH-GASVERIFY-A0 is safe for storage or pressure operation.
GH-GASVERIFY-A0 replaces calibrated laboratory analysis.
```

Verification Philosophy

The rack exists to separate observation from proof.

Visible bubbles are observation.

Hydrogen-specific detection is evidence.

Calibrated hydrogen measurement is stronger evidence.

Repeatable, calibrated, source-traceable, safety-gated data is stronger still.

Rack Design Rules

GH-GASVERIFY-A0 must be:

non-pressurized,
inspectable,
short-path,
leak-checked,
vented safely,
protected from liquid carryover,
stable during A/B tests,
and documented with photos or sketches.

GH-GASVERIFY-A0 must not be:

sealed,
compressed,
used for storage,
used for flame testing,
hidden inside opaque routing,
connected to ignition sources,
or treated as certified gas analysis unless independently validated.
Gas Verification Position in the System

```
baseline electrolysis reference
  -> baseline separator or GANKYIL-A
  -> liquid carryover protection
  -> hydrogen verification point
  -> optional oxygen-side observation record
  -> safe non-pressurized vent path
```

Required Precondition

Before assembling the verification rack, confirm:

baseline rig zone layout exists,
gas generation hardware is stable,
separator or Gankyil-A path is selected,
gas path is non-pressurized,
ventilation is confirmed,
no flame-test material is present,
emergency disconnect is reachable,
hydrogen detector or sensor is selected,
leak-check method is selected,
evidence forms are ready,
and the operator understands stop conditions.

If any required precondition fails, do not assemble for a live run.

Rack Zones

The gas verification rack should be divided into five visible micro-zones:
```
+--------------------------------------------------------------+
| Micro-Zone 1: Incoming Gas Path                              |
| - from baseline separator or GANKYIL-A                       |
| - labeled tubing direction                                   |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Micro-Zone 2: Liquid Carryover Protection                    |
| - trap, demister, or visible moisture barrier                 |
| - wetness inspection point                                   |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Micro-Zone 3: Hydrogen Verification Point                    |
| - hydrogen detector / sensor                                 |
| - stable sensor mount                                        |
| - sensor record                                              |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Micro-Zone 4: Optional Oxygen / Crossover Awareness          |
| - oxygen-side record or sensor                               |
| - separation integrity notes                                 |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Micro-Zone 5: Safe Non-Pressurized Vent Path                 |
| - no storage                                                 |
| - no ignition source                                         |
| - no blocked outlet                                          |
+--------------------------------------------------------------+
```

Step 0: Select Verification Mode

Select one verification mode before assembly.

Mode 1: Qualitative Hydrogen Detection

Used when the system has a hydrogen-specific detector but no calibrated quantitative output.

Allowed result:
```
hydrogen-specific detection observed
```

Not allowed:
```
hydrogen concentration quantified
hydrogen purity proven
production rate proven
```

Mode 2: Semi-Quantitative Sensor Evidence

Used when the hydrogen sensor has a documented range and calibration or bump-test state is recorded.

Allowed result:
```
hydrogen response recorded within the documented sensor limits
```
Not allowed unless supported:
```
certified gas composition
validated purity
standards-grade production rate
```

Mode 3: Stronger Flow / Volume Evidence

Used when hydrogen detection is paired with a low-flow or volume method that does not create unsafe pressure.

Allowed result:
```
bounded hydrogen output estimate under documented bench conditions
```

Still not allowed:
```
commercial output claim
efficiency claim without full energy and gas accounting
green-hydrogen claim without source traceability
```

Step 1: Prepare the Mounting Rack

Install a rigid mount, rail, board, or frame in the gas verification zone.

The rack should hold:

incoming tubing,
liquid carryover protection,
hydrogen detector or sampling point,
optional oxygen-side record device,
vent path label,
and sensor labels.

The rack must not:

pinch tubing,
block venting,
create a sealed volume,
route gas near ignition sources,
or force liquid toward the sensor.

Take a photo of the empty rack before installing tubing.

Step 2: Label the Gas Direction

Label tubing direction clearly.

Required labels:
```
FROM GENERATION
FROM BASELINE SEPARATOR
FROM GANKYIL-A
TO HYDROGEN SENSOR
TO SAFE VENT
NO PRESSURE STORAGE
```
Use only the labels that match the current configuration.

Do not use ambiguous labels such as:
```
output
gas thing
test tube
hydrogen tank
storage
```

The word "tank" should not appear in GH-BENCH-A0 unless documenting forbidden equipment.

Step 3: Install Incoming Gas Path

Connect the incoming gas path from either:
```
baseline separator path
```
or:
```
GANKYIL-A phase-management path
```
Use short, inspectable tubing.

Record:
```
upstream_source
incoming_tubing_material
incoming_tubing_length
incoming_fitting_type
incoming_path_visible
operator_notes
```
Reject the setup if the incoming path is hidden, kinked, unlabeled, or able to trap pressure.

Step 4: Install Liquid Carryover Protection

Place a liquid trap, demister, knock-out section, or visible moisture inspection point before the hydrogen sensor.

Purpose:

prevent sensor wetting,
preserve reading credibility,
reduce liquid carryover ambiguity,
and protect downstream verification hardware.

Record:
```
liquid_protection_type
liquid_protection_location
visible_inspection_possible
drain_or_cleaning_method
operator_notes
```

The liquid protection stage must not create pressure storage.

If liquid reaches the sensor, the run should be stopped and marked rejected or inconclusive.

Step 5: Install Hydrogen Detector or Sensor

Mount the hydrogen detector or sensor according to its documentation.

Record:
```
hydrogen_sensor_model
hydrogen_sensor_role
sensor_range
sensor_warmup_required
sensor_calibration_state
sensor_bump_test_state
sensor_position
sensor_distance_from_liquid_trap
sensor_orientation
sensor_limitations
operator_notes
```
If the selected detector is an area monitor rather than a process sensor, record that honestly.

Do not represent an area alarm as a calibrated process analyzer.

Step 6: Protect Sensor From Wet Gas

Confirm that the hydrogen sensor is protected from:

direct droplets,
liquid slugs,
condensate pooling,
tubing backflow,
and accidental splashing.

Record:
```
sensor_wetness_protection_confirmed
wetness_inspection_point_present
sensor_inlet_clear
downstream_path_unblocked
operator_notes
```

If sensor wetness risk cannot be controlled, do not run.

Step 7: Install Optional Flow or Volume Measurement

If using flow or volume measurement, install it only if it does not create unsafe backpressure.

Record:
```
flow_measurement_present
flow_measurement_method
flow_device_model_or_description
flow_device_range
flow_device_pressure_risk
flow_device_wet_gas_compatibility
operator_notes
```

Reject the measurement method if it:

blocks the outlet,
creates pressure buildup,
traps gas,
is not compatible with wet gas,
or makes the gas path unclear.
Step 8: Install Optional Oxygen-Side Observation

If the selected electrolysis reference provides an oxygen-side path or observation point, record it.

Fields:
```
oxygen_observation_present
oxygen_sensor_model_or_method
oxygen_side_path_description
oxygen_side_behavior
crossover_concern
operator_notes
```
Oxygen-side observation is not optional for strong evidence.

It may be qualitative at A0, but it must not be ignored if the hardware exposes an oxygen-side condition.

Step 9: Define Safe Vent Path

The downstream gas path must remain safely vented and non-pressurized.

Record:
```
vent_path_defined
vent_path_location_description
vent_path_unblocked
vent_path_away_from_ignition_sources
ventilation_present
operator_notes
```
The vent path must not terminate near:

sparks,
flames,
hot surfaces,
switches likely to arc,
outlets,
motors,
or enclosed pockets.

Follow local safety rules and component documentation.

Step 10: Verify No Storage

Confirm the rack contains no hydrogen storage.

Required confirmations:
```
no_pressure_storage = true
no_compression = true
no_sealed_collection = true
no_flame_test = true
no_blocked_outlet = true
```
If any field is false, the rack is rejected for GH-BENCH-A0.

Step 11: Perform Sensor Warmup and Plausibility Check

If the hydrogen sensor requires warmup, complete it before the run.

Record:
```
sensor_warmup_started
sensor_warmup_completed
baseline_reading
ambient_condition_note
sensor_ready
operator_notes
```
If the sensor reading is unstable before gas production begins, do not use it for an accepted hydrogen claim.

Step 12: Perform Calibration or Bump-Test Record

If calibration or bump-test support is available, record it.

Fields:
```
calibration_available
calibration_date
calibration_method
bump_test_available
bump_test_result
calibration_expired
operator_notes
```
If calibration is not available, mark it clearly.

Example:
```
calibration_available = false
claim_limit = qualitative_detection_only
```
Do not turn an uncalibrated reading into a quantitative claim.

Step 13: Leak Check the Verification Rack

Leak-check the assembled verification rack according to the selected fittings and component documentation.

Record:
```
leak_check_method
leak_check_locations
leak_check_result
leak_check_time
operator_notes
```
The run is blocked if:

leak check fails,
leak check is skipped,
any fitting is changed after leak check,
or the gas path becomes unclear.
Step 14: Rack Preflight Checklist

Before a run, complete:
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
If any required field fails, the run is blocked.

Step 15: Create Gas Record File

Each run should include a gas record.

Recommended file:
```
run_bundles/<run_id>/gas_record.json
```
Minimum fields:
```
run_id
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
Step 16: Record Starting State

Before gas generation, record:
```
start_time
hydrogen_sensor_initial_reading
oxygen_sensor_initial_reading_or_observation
ambient_temperature
ambient_humidity_if_available
gas_path_dry_or_wet_state
liquid_trap_initial_state
vent_path_confirmed
operator_notes
```
A starting state is required to interpret later readings.

Step 17: During-Run Gas Observations

At defined intervals, record:
```
timestamp
hydrogen_sensor_reading
oxygen_sensor_reading_or_observation
visible_bubble_behavior
liquid_carryover
sensor_wetness
flow_or_volume_reading
gas_path_stability
vent_path_state
operator_notes
```
Do not adjust the gas rack during a run unless stopping for safety.

If the rack changes, the run should receive a new run ID after correction.

Step 18: Stop Conditions

Stop the run if:

hydrogen accumulation is suspected,
area alarm activates,
sensor becomes wet,
liquid reaches verification point,
tubing disconnects,
outlet becomes blocked,
leak is suspected,
ventilation changes,
sensor reading becomes unstable or saturated,
flow device appears to restrict gas,
electrical behavior changes unexpectedly,
operator loses line of sight,
or any safety concern appears.

A stopped run should be preserved as evidence.

Step 19: Normal Shutdown Record

After normal shutdown, record:
```
stop_time
hydrogen_sensor_final_reading
oxygen_sensor_final_reading_or_observation
liquid_trap_final_state
sensor_wetness_final_check
leak_or_damage_observed
venting_completed
operator_notes
```
Do not seal the gas path after shutdown until it is safe and cleared according to the selected procedure.

Step 20: Post-Run Sensor Inspection

Inspect:

hydrogen sensor inlet or face,
tubing near the sensor,
liquid trap,
downstream vent path,
fittings,
rack mount,
and any flow/volume device.

Record:
```
sensor_wetness_observed
sensor_residue_observed
liquid_in_downstream_path
fittings_shifted
flow_device_condition
cleaning_required
ready_for_next_run
operator_notes
```
If sensor wetness or residue is observed, the run should not support a clean hydrogen detection claim without review.

Step 21: Gas Evidence Acceptance

Gas evidence may be accepted only if:

hydrogen-specific detector or sensor was used,
sensor state was recorded,
gas path was documented,
leak check passed,
liquid did not corrupt the sensor,
vent path remained unblocked,
safety preflight passed,
and operator notes exist.

If any item is missing, the gas result should be:
```
inconclusive
```
or:
```
blocked_by_missing_evidence
```
depending on the failure.

Step 22: Gas Evidence Rejection

Reject gas evidence if:

visible bubbles are the only evidence,
sensor was missing,
sensor model is unknown,
sensor was wet,
sensor was saturated,
gas path was unknown,
leak check failed,
outlet was blocked,
flow device caused restriction,
ventilation was missing,
or the operator changed the rack during the run without a new run ID.
Step 23: Allowed Gas Claims by Evidence Level
Evidence Level	Allowed Claim	Forbidden Claim
Visual bubbles only	Gas evolution observed	Hydrogen confirmed
Hydrogen detector present, uncalibrated	Hydrogen-specific response observed	Concentration or purity proven
Calibrated hydrogen sensor	Bounded hydrogen reading recorded	Certified purity or production rate unless supported
Sensor plus flow/volume estimate	Bounded output estimate	Efficiency unless full input/output accounting exists
Repeat calibrated runs	Repeatable bounded result	Field-ready or commercial claim
Step 24: Rack Photo Requirements

Recommended photos:
```
01_empty_rack.jpg
02_labeled_incoming_path.jpg
03_liquid_protection_stage.jpg
04_hydrogen_sensor_mount.jpg
05_vent_path.jpg
06_full_verification_rack_before_run.jpg
07_full_verification_rack_after_run.jpg
```
Photos should show labels and layout, not just close-ups.

Do not take photos in a way that distracts the operator during active testing.

Step 25: Rack Maintenance

After use:

clean liquid trap if used,
dry tubing if appropriate,
inspect sensor area,
replace damaged tubing,
remove any residue,
mark questionable parts,
and update maintenance notes.

Maintenance record fields:
```
part_inspected
condition
cleaning_performed
replacement_required
do_not_use_marked
operator_notes
```
Do not reuse parts marked questionable until reviewed.

Assembly Acceptance Checklist

Before declaring GH-GASVERIFY-A0 ready:

 Incoming gas path is labeled.
 Gas path is non-pressurized.
 No storage volume is present.
 Liquid protection is installed.
 Hydrogen detector or sensor is installed.
 Sensor model is recorded.
 Sensor calibration or limitation state is recorded.
 Sensor wetness protection is confirmed.
 Optional flow method does not create backpressure.
 Oxygen-side observation is defined.
 Vent path is defined.
 Vent path is away from ignition sources.
 Ventilation is confirmed.
 Leak check passed.
 Evidence forms are ready.
 Operator understands stop conditions.
Assembly Rejection Checklist

Reject the gas verification rack if:

 Gas path is sealed.
 Gas can accumulate in storage.
 Outlet can be blocked.
 Flame test is planned.
 Hydrogen sensor is missing.
 Sensor model is unknown.
 Sensor can be wetted easily.
 Leak check is skipped.
 Vent path is unclear.
 Ventilation is missing.
 Flow device creates restriction.
 Evidence file cannot be created.
 Operator cannot explain the rack.
Final Rule

The gas verification rack is not there to make the result look impressive.

It is there to make the result reviewable.

If the rack cannot clearly tell the difference between hydrogen evidence, wet-sensor noise, leaked gas, missing data, and unsafe setup, it is not ready.


