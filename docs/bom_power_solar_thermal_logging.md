# BOM: Power, Solar, Thermal, and Data Logging

## Purpose

This document defines the supplier-neutral power, solar, thermal, and data-logging bill of materials for the Green-Hydrogen first bench validation rig.

The purpose is not to create a high-output energy system.

The purpose is to make every energy input visible, bounded, measurable, and reviewable.

A hydrogen run is not a green-hydrogen run unless the energy source is known and recorded.

## Target Rig

```
GH-BENCH-A0
```
GH-BENCH-A0 is a low-output, non-pressurized, supervised bench validation platform.

It is not:

a commercial hydrogen production unit,
a grid-scale renewable system,
a pressure appliance,
an unattended generator,
a certified electrolyzer,
or a field deployment.
Power Philosophy

The power system should answer five questions:

Where did the energy come from?
How much electrical energy entered the system?
Was the energy stable during the run?
Was any thermal input present?
Can the energy claim survive review?

If the answer is unknown, the repo must say unknown.

Unknown energy cannot be called green.

Power Architecture Overview
```
+-----------------------------+
| Energy Source               |
| - bench DC supply           |
| - battery                   |
| - solar panel               |
| - grid-backed supply        |
| - mixed source              |
+--------------+--------------+
               |
               v
+-----------------------------+
| Protection Layer            |
| - fuse                      |
| - current limit             |
| - emergency disconnect      |
| - cable strain relief       |
+--------------+--------------+
               |
               v
+-----------------------------+
| Measurement Layer           |
| - voltage                   |
| - current                   |
| - power                     |
| - watt-hours                |
| - duration                  |
+--------------+--------------+
               |
               v
+-----------------------------+
| Electrolysis Reference      |
| - baseline cell/module      |
| - measured input only       |
+--------------+--------------+
               |
               v
+-----------------------------+
| Evidence Bundle             |
| - power record              |
| - source record             |
| - carbon note               |
| - acceptance result         |
+-----------------------------+
```
Category 1: Baseline Electrical Power
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Current-limited DC bench power supply	1	Low-voltage, current-limited supply compatible with selected electrolysis module	Provides controlled baseline input	Must show voltage/current or be paired with external meter.
Inline DC power meter	1	Measures voltage, current, power, and watt-hours	Records electrical input	Required for energy evidence.
Multimeter	1	Independent digital multimeter	Cross-checks supply and wiring	Must be known working.
Inline fuse holder	1	Compatible with low-voltage DC line	Overcurrent protection	Required before powered test.
Fuse assortment	1 set	Matched to selected circuit limits	Protection replacement	Ratings must be recorded.
Emergency disconnect switch	1	Physical cutoff accessible from operator position	Fast shutdown	Required.
Insulated DC leads	1 set	Properly rated leads with secure connectors	Connects supply to electrolysis module	Must be strain-relieved.
Cable strain relief hardware	1 set	Clips, clamps, or tie points	Prevents accidental pulling	Required near wet zone.
Cable labels	1 set	Labels for positive, negative, sensor, and disconnect paths	Prevents connection errors	Required before first run.
Baseline Electrical Rules

The first baseline run should use a controlled bench power supply before solar or battery testing.

Reasons:

stable input,
easier energy accounting,
easier repeatability,
easier shutdown,
easier fault isolation,
and cleaner baseline comparison.

Do not use a solar panel as the first power source unless the power path can be measured and stabilized.

Category 2: Power Protection and Shutdown
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Emergency stop / disconnect	1	One-action power cutoff	Stops the run quickly	Must be reachable without crossing wet zone.
Inline overcurrent protection	1	Fuse or breaker matched to circuit	Protects wiring and module	Required.
Current limit setting record	1	Written or digital record of supply limit	Documents safety boundary	Required before run.
Cable routing clips	1 set	Nonconductive clips or mounts	Keeps wires away from water	Required.
Drip loop routing	As needed	Physical routing method	Prevents water running into electronics	Required where cables descend near wet zone.
Nonconductive mounting board	1	Dry-side electronics mount	Keeps power hardware organized	Strongly preferred.
Red emergency label	1	Label for shutdown control	Operator clarity	Required.
Post-run power-down checklist	1	Printed or digital checklist	Confirms safe shutdown	Required.
Shutdown Rule

The operator must be able to cut power without touching the gas path, electrolysis cell, or wet zone.

If shutdown requires reaching across the wet zone, the layout is rejected.

Category 3: Electrical Measurement and Evidence
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Voltage measurement method	1	Bench supply display, multimeter, or logger	Records voltage	Must be timestamped or tied to run interval.
Current measurement method	1	Bench supply display, inline meter, multimeter, or logger	Records current	Must record current limit and observed value.
Power calculation method	1	Meter or calculation from voltage/current	Estimates watts	Must state whether measured or calculated.
Watt-hour logging method	1	Inline meter or time-series calculation	Estimates total energy	Required for efficiency discussion.
Timekeeping method	1	Clock, timer, or logger	Records run duration	Required.
Power record form	1	Printed or digital form	Captures electrical evidence	Required.
Instrument inventory sheet	1	Lists meter make/model if available	Evidence provenance	Required for serious review.
Electrical Evidence Rule

No energy claim is allowed without:

voltage,
current,
duration,
and source record.

No efficiency claim is allowed without:

electrical input,
thermal input if present,
gas output,
water input,
and uncertainty notes.
Category 4: Battery Power Path

Battery testing is optional and should not be part of the first baseline unless the battery source and protection are clear.

Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Protected DC battery pack	Optional	Battery system with appropriate protection for selected load	Future stored-energy test	Not required for baseline.
Battery state-of-charge record method	Optional	Built-in display or external measurement	Documents battery condition	Required if battery is used.
Battery charger record	Optional	Documents how battery was charged	Supports energy traceability	Required for green claim.
Battery fuse/protection	Optional	Matched to battery and load	Safety protection	Required if battery is used.
Battery disconnect	Optional	Physical cutoff	Safe isolation	Required if battery is used.
Battery containment / placement tray	Optional	Stable dry-side location	Prevents accidental contact with wet zone	Required if battery is used.
Battery Rules

Do not call a battery run renewable unless the battery charging source is known.

A battery charged from the grid is not automatically green.

A battery charged from solar must have a source record.

Category 5: Solar Electrical Input

Solar input is optional for GH-BENCH-A0 and should be introduced only after stable bench-supply baseline evidence exists.

Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Small DC solar panel	Optional	Bench-scale panel appropriate for later low-power testing	Renewable input comparison	Not required for baseline.
Solar charge controller or MPPT module	Optional	Matched to panel and battery/load	Controls solar input	Must be documented.
Solar voltage/current meter	Optional	Measures panel or controller output	Records solar input	Required for solar claim.
Solar irradiance meter or log method	Optional	Measures or records sunlight condition	Context for solar performance	Strongly preferred.
Panel angle/orientation record	Optional	Written orientation note	Repeatability	Required for comparison.
Weather/sky condition note	Optional	Clear/cloudy/time/location record	Solar context	Required for solar run notes.
Solar source log form	1	Printed or digital form	Records renewable source	Required for green claim.
Solar Input Rules

Solar is not allowed to be vague.

A solar-assisted electrical run must record:

panel type or rating,
panel orientation,
time of day,
weather/sky condition,
measured voltage,
measured current,
duration,
whether battery buffering was used,
and whether the electrolyzer saw direct or stored solar power.

Do not claim green hydrogen from solar unless the solar path is actually used and recorded.

Category 6: Solar Thermal Assist

Solar thermal assist is optional and disabled by default.

It may be tested only after baseline evidence is stable.

Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Solar thermal collector surface	Optional	Small, controlled, low-temperature collector surface	Future thermal assist comparison	Not part of baseline.
Thermal interface plate or jacket	Optional	Controlled contact method for warming water or cell area	Transfers heat in repeatable way	Must not damage electrolysis module.
Temperature probe, input side	Optional	Measures thermal source temperature	Records thermal input condition	Required for thermal branch.
Temperature probe, cell/water side	Optional	Measures system temperature	Tracks effect on run	Required for thermal branch.
Ambient temperature/humidity meter	1	Room condition measurement	Context for thermal behavior	Recommended for all runs.
Insulation material	Optional	Nonflammable/compatible insulation where appropriate	Reduces thermal drift	Must not trap gas or create unsafe heating.
Thermal branch record form	1	Printed or digital form	Captures thermal evidence	Required if thermal assist is used.
Solar Thermal Rules

Solar thermal input must be counted.

A thermal-assisted run must record:

thermal source,
measured temperature,
location of temperature probe,
exposure duration,
thermal contact method,
ambient conditions,
and whether the thermal path changed sensor behavior.

Do not claim efficiency improvement if thermal energy is unmeasured or ignored.

Category 7: Thermal Safety and Drift Monitoring
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Water temperature probe	1	Water-compatible probe	Tracks water/electrolyte temperature	Required.
Cell surface temperature method	Optional	Contact or non-contact temperature measurement	Detects abnormal heating	Strongly preferred.
Gas path temperature probe	Optional	Low-range gas path measurement	Supports gas interpretation	Useful for stronger evidence.
Ambient thermometer/hygrometer	1	Room condition measurement	Supports repeatability	Strongly preferred.
Thermal stop-condition checklist	1	Defines when to stop for heat	Safety support	Required if thermal assist is used.
Thermal anomaly log	1	Records unexpected heating/cooling	Preserves evidence	Required if thermal behavior is abnormal.
Thermal Stop Conditions

Stop the run if:

temperature rises unexpectedly,
plastic parts soften or deform,
condensation reaches sensors,
tubing behavior changes,
the electrolysis module exceeds its documented limits,
operator smells burning or sees discoloration,
power draw changes unexpectedly with temperature,
or any thermal condition becomes unclear.
Category 8: Data Logging Hardware
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Laptop or tablet	1	Local evidence capture	Records forms, notes, and files	Keep outside wet zone.
USB data logger or microcontroller logger	Optional	Logs voltage, current, temperature, or sensor signals	Improves time-series evidence	Manual logging acceptable at A0.
SD card or local storage	Optional	Local evidence storage	Preserves raw data	Must be backed up after run.
Timestamp method	1	System clock, logger time, or written standard	Aligns records	Required.
Camera or phone camera	1	Setup photos and anomaly record	Visual context	Must not distract operator.
Fixed camera mount	Optional	Repeatable visual record	Supports A/B comparison	Strongly preferred for Gankyil testing.
Printed manual log sheets	1 set	Backup records	Protects against software failure	Required.
File folder template	1	Run-bundle directory convention	Organizes evidence	Required.
Data Logging Rule

Manual logging is allowed for GH-BENCH-A0 if it is disciplined.

A manual log must include:

timestamp,
voltage,
current,
water temperature,
gas observation,
sensor reading,
anomalies,
and operator initials or note.

Automated logging is better, but incomplete automation is not better than complete manual evidence.

Category 9: Data Fields to Capture

Minimum power/thermal logging fields:

```
run_id
date_time
operator
source_type
source_description
voltage_v
current_a
power_w
duration_s
energy_wh
current_limit_a
fuse_rating_a
emergency_disconnect_confirmed
battery_used
battery_charge_source
solar_used
solar_voltage_v
solar_current_a
solar_condition_note
thermal_assist_used
thermal_source
thermal_source_temp_c
water_temp_c
cell_surface_temp_c
ambient_temp_c
ambient_humidity_percent
instrument_notes
operator_notes
```

Category 10: Evidence File Outputs

A complete power and logging package should produce:
```
run_bundles/<run_id>/
  power_record.json
  energy_source_record.json
  thermal_record.json
  carbon_record.json
  sensor_log.csv
  manual_notes.md
  setup_photos/
  acceptance.json
```
For early manual tests, sensor_log.csv may be replaced by a scanned or photographed manual sheet.

If a file is missing, the acceptance result must say so.

Category 11: Carbon Accounting Support
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Energy source record form	1	Captures source type and traceability	Supports green-hydrogen claim discipline	Required.
Grid/battery/solar classification field	1	Source category	Prevents vague source claims	Required.
Renewable fraction estimate method	1	Conservative estimate or unknown marker	Supports carbon note	Required.
Carbon accounting script	1	Converts energy/source record into bounded estimate	Evidence support	Must mark unknowns honestly.
Carbon assumption note	1	Documents assumptions and limitations	Prevents overclaiming	Required.
Carbon Accounting Rule

A hydrogen run can be physically real and still fail the green claim.

The system must distinguish:

hydrogen detected,
hydrogen measured,
hydrogen produced with known energy,
hydrogen produced with renewable-traceable energy,
and hydrogen produced with defensible carbon accounting.

These are not the same claim.

Category 12: Optional Controller Hardware

Controller hardware is optional and should not replace manual safety.

Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Microcontroller or single-board logger	Optional	Reads low-risk sensors and writes logs	Automation support	Must not control unsafe hardware autonomously.
Relay module	Optional	Low-voltage control only, if used	Future controlled shutdown	Must fail safe.
Sensor interface board	Optional	Connects sensors to logger	Data capture	Must not bypass calibration.
Real-time clock module	Optional	Stable timestamp	Data alignment	Useful for logger.
Enclosure for electronics	Optional	Keeps electronics organized	Dry-side protection	Must not trap heat.
Controller Rules

A controller may log.

A controller may help enforce safe shutdown after review.

A controller must not:

run unattended hydrogen production,
override emergency stop,
enable plasma branch by default,
hide raw sensor data,
or accept claims automatically without evidence review.
Category 13: Power/Solar/Thermal Items Not Allowed in A0

Do not include in GH-BENCH-A0:

high-voltage supplies,
high-current output chasing,
exposed mains wiring,
improvised transformers,
plasma power supplies,
microwave sources,
uncontrolled heaters,
sealed heated vessels,
hydrogen storage batteries or fuel-cell loops,
compressed gas hardware,
or any energy-recovery device advertised with unsupported claims.
Category 14: Procurement Priority

Recommended procurement order:

Current-limited DC bench supply.
Inline DC power meter.
Emergency disconnect.
Fuse/protection hardware.
Multimeter.
Cable labels and routing hardware.
Water temperature probe.
Ambient temperature/humidity meter.
Manual logging materials.
Laptop/tablet evidence setup.
Optional data logger.
Optional solar electrical hardware.
Optional solar thermal hardware.

Do not buy optional solar or thermal parts before the baseline electrical path is safe and measurable.

Baseline Power Test Procedure

Before connecting the electrolysis reference module:

Place power hardware on dry side.
Confirm emergency disconnect is reachable.
Confirm fuse rating is installed and recorded.
Set current limit.
Confirm output voltage is off.
Connect inline power meter.
Confirm polarity.
Confirm cable strain relief.
Confirm no cable crosses wet zone unnecessarily.
Power on without electrolysis load if appropriate.
Verify meter reading plausibility.
Power off.
Record readiness.
Solar Electrical Test Procedure

Solar electrical testing should occur only after baseline runs.

Required sequence:

Confirm baseline evidence exists.
Define solar run intent.
Record panel and controller configuration.
Record weather and time.
Measure solar voltage/current.
Confirm stable load path.
Confirm emergency disconnect.
Run only within the same non-pressurized gas boundary.
Record output and evidence.
Compare against baseline without overclaiming.
Solar Thermal Test Procedure

Solar thermal testing should occur only after stable baseline runs.

Required sequence:

Confirm baseline evidence exists.
Define thermal run intent.
Confirm no plasma or advanced branch is active.
Record thermal source.
Record ambient temperature.
Record water/cell starting temperature.
Apply thermal input in controlled bounded way.
Record temperature over time.
Record electrical input separately.
Count thermal input as part of interpretation.
Stop if thermal behavior becomes unclear.
Preserve evidence whether accepted or rejected.
Data Logging Procedure

Before run:

Create run ID.
Create run folder.
Confirm timestamp method.
Confirm manual forms or logger.
Record instrument list.
Record calibration state.
Start notes file.

During run:

Record start time.
Record voltage/current at defined intervals.
Record water/gas observations.
Record sensor readings.
Record anomalies immediately.
Record stop time.

After run:

Save raw logs.
Photograph or scan manual sheets if used.
Save setup photos.
Generate evidence bundle.
Generate acceptance result.
Mark claim status.
Acceptance Criteria

The power, solar, thermal, and logging BOM is acceptable when it supports:

controlled baseline electrical input,
emergency shutdown,
overcurrent protection,
power measurement,
source traceability,
optional solar record,
optional thermal record,
timestamped run evidence,
carbon accounting,
and honest rejection of missing data.
Failure Criteria

This BOM is not acceptable if:

power source is unknown,
voltage/current are not measured,
emergency disconnect is missing,
fuse/protection is missing,
water and electrical paths are mixed,
solar is claimed without solar records,
thermal assist is used without thermal records,
battery source is unknown but claimed green,
data logging is absent,
or the setup encourages efficiency claims without output measurement.
Minimum Baseline Power Evidence

A minimum valid baseline power record includes:

```
run_id
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

Stronger Baseline Power Evidence

A stronger baseline power record includes:
```
run_id
source_type
source_traceability
voltage_time_series
current_time_series
power_time_series
energy_wh
current_limit_a
meter_model
meter_calibration_state
ambient_temp_c
water_temp_c
gas_sensor_timestamp_alignment
operator_notes
uncertainty_note
```

First Green-Hydrogen Claim Requirements

The repo may not call a run green hydrogen unless the evidence includes:

Hydrogen measurement.
Water record.
Electrical energy record.
Energy source record.
Renewable traceability.
Carbon accounting note.
Safety record.
Acceptance result.
Claim boundary.

If renewable traceability is incomplete, the run may be hydrogen evidence but not green-hydrogen evidence.

Final Rule

Power is evidence.

Solar is evidence only when measured.

Thermal assist is evidence only when counted.

A run with unknown energy source is not a green-hydrogen proof package.
