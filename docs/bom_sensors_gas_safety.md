# BOM: Sensors, Gas Verification, and Safety Hardware

## Purpose

This document defines the supplier-neutral sensor, gas-verification, and safety hardware needed for the first Green-Hydrogen bench validation rig.

This BOM does not authorize a build by itself.

It exists to make the first proof-of-concept path safer, more measurable, and harder to overclaim.

## Rig Boundary

Target rig:

```
GH-BENCH-A0
```

GH-BENCH-A0 is a non-pressurized, low-output, supervised bench validation setup.

It is not:

a pressure system,
a hydrogen storage system,
a certified gas appliance,
an unattended hydrogen generator,
a commercial electrolyzer,
or a field-deployable energy system.
Procurement Principle

The first sensor and safety package should prioritize:

Credible hydrogen detection.
Leak awareness.
Ventilation confirmation.
Electrical shutdown.
Water/electrical separation.
Repeatable evidence.
Sensor calibration records.
Failed-run preservation.
Clear stop conditions.
Conservative claim boundaries.

Do not select parts because they sound advanced.

Select parts because they reduce ambiguity.

Minimum Sensor Stack

The minimum recommended sensor stack for a first credible bench test is:

Sensor / Tool	Minimum Role	Why It Matters
Hydrogen detector or sensor	Confirms hydrogen presence	Prevents bubble-only claims.
Area hydrogen alarm or independent monitor	Safety awareness	Detects unexpected accumulation risk.
Oxygen sensor or oxygen-side observation method	Tracks oxygen-side behavior	Helps identify crossover or abnormal gas behavior.
DC voltage/current/power meter	Measures electrical input	Required for energy accounting.
Water temperature sensor	Documents water condition	Helps repeatability and sensor interpretation.
pH meter or pH strips	Documents water chemistry	Prevents unknown-water claims.
Conductivity/TDS meter	Documents water conductivity	Supports baseline repeatability.
Ambient thermometer/hygrometer	Records room conditions	Helps interpret condensation and sensor drift.
Leak-check method	Confirms gas path integrity	Prevents false gas readings and unsafe operation.
Timestamped logging method	Aligns evidence	Makes run review possible.
Stronger Sensor Stack

A stronger review-ready bench package adds:

Sensor / Tool	Stronger Role	Why It Matters
Calibratable hydrogen sensor	Quantitative or semi-quantitative hydrogen evidence	Supports stronger hydrogen claims.
Low-flow gas meter or volume method	Output estimate	Allows rate comparison and repeatability analysis.
Gas temperature sensor	Gas-path condition	Supports flow and sensor interpretation.
Differential pressure indicator, low range	Restriction warning only	Confirms no unintended buildup.
Data logger	Time-series evidence	Reduces manual logging errors.
Camera or fixed visual record	Setup and anomaly documentation	Helps reviewers understand configuration.
Independent power logger	Cross-checks supply display	Prevents relying on one instrument.
Calibration gas or vendor-approved bump-test tool, where appropriate	Sensor confidence	Needed before quantitative claims.
Category 1: Hydrogen Detection
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Process hydrogen detector or sensor	1	Hydrogen-specific detector/sensor with documented range and response behavior	Confirms hydrogen presence in verification path	Exact model, range, warmup, and limitations must be logged.
Area hydrogen alarm or independent monitor	1	Independent hydrogen safety monitor appropriate for the workspace	Detects unexpected accumulation	Strongly preferred as separate from process sensor.
Sensor mounting bracket	1	Rigid, repeatable mounting hardware	Prevents sensor movement between runs	Position must be recorded in run evidence.
Sensor splash/wetness protection	1	Physical arrangement or compatible trap to prevent liquid reaching sensor	Prevents false or damaged readings	Must not create unsafe restriction.
Hydrogen calibration or bump-test method	1	Vendor-supported method if available	Supports sensor confidence	Required before quantitative claims.
Hydrogen sensor log sheet	1	Printed or digital form	Records sensor state	Must include model, serial if available, calibration state, and run ID.
Hydrogen Detection Rules

Visible bubbles are not accepted as hydrogen proof.

A hydrogen claim requires hydrogen-specific evidence.

A quantitative hydrogen claim requires:

known sensor model,
known range,
known calibration or bump-test state,
documented sensor placement,
gas path description,
humidity/wetness note,
and run timestamp.

If those are missing, the result may only be described as preliminary observation.

Category 2: Oxygen and Crossover Awareness
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Oxygen sensor or oxygen-side detector	1	Oxygen measurement method appropriate to the selected cell or gas path	Tracks oxygen-side behavior	Required for stronger evidence.
Oxygen-side visual observation point	1	Visible, non-pressurized observation path	Allows qualitative review	Must not be used as pressure storage.
Oxygen-side record sheet	1	Printed or digital form	Records oxygen-side notes	Must record abnormal bubbling, moisture, or crossover concerns.
Separation integrity checklist	1	Checklist tied to selected electrolysis module	Confirms intended gas separation path	Must be completed before accepted run.
Oxygen-Side Rules

The oxygen side is not ignored.

The first rig must record whether oxygen-side behavior was:

normal,
abnormal,
not measured,
inconclusive,
or unsafe.

Any suspected gas crossover should trigger a stopped or rejected run.

Category 3: Flow, Volume, and Gas Path Evidence
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Low-flow gas measurement device or method	1	Compatible with low-volume wet gas or protected from wet gas	Estimates output rate or volume	Must not create unsafe backpressure.
Transparent liquid trap / knock-out trap	1	Non-pressurized transparent trap	Prevents liquid carryover into sensor	Must be inspectable and drainable after shutdown.
Gas humidity / condensation note method	1	Manual observation or simple humidity-aware record	Documents wet gas condition	Required because wet gas can affect sensors.
Gas temperature probe	Optional	Low-range temperature probe near gas path	Records gas condition	Useful for repeatability.
Tubing direction labels	1 set	Arrow labels for gas path direction	Prevents wrong reconnection	Required before A/B tests.
Gas path diagram sheet	1	Simple drawing or printed template	Records actual routing	Required for evidence bundle.
Gas Path Rules

The gas path must remain:

non-pressurized,
short,
visible where practical,
leak-checked,
vented safely,
and free of intentional storage.

Do not add restrictions merely to improve measurement.

Any measurement method that causes pressure buildup is rejected for GH-BENCH-A0.

Category 4: Leak Check and Venting
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Leak-check method	1	Compatible method for selected fittings and tubing	Detects gas-path leaks	Must not contaminate sensor path.
Leak-check record sheet	1	Printed or digital form	Records pass/fail and location checked	Required before powered run.
Ventilation method	1	Location-appropriate ventilation selected by qualified review	Reduces accumulation risk	Must be confirmed before run.
Vent path marker	1	Label or visual marker for exhaust/vent direction	Prevents accidental obstruction	Required if vent path is not obvious.
No-ignition-source signage	1 set	Visible safety signage	Area awareness	Required during physical testing.
Post-run venting checklist	1	Checklist for shutdown and clearing	Prevents residual gas ambiguity	Required after run.
Ventilation Rule

Do not operate GH-BENCH-A0 in an unventilated space.

Do not assume a room is safe because the rig is small.

Ventilation must be treated as a preflight requirement, not an afterthought.

Category 5: Electrical Measurement and Shutdown
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Current-limited DC supply	1	Low-voltage current-limited supply matched to selected electrolysis reference	Controlled electrical input	Must have readable output display.
Inline DC watt-hour meter or logger	1	Measures voltage, current, power, and duration	Energy accounting	Required for any efficiency or energy statement.
Multimeter	1	Independent voltage/current/resistance checks	Cross-checks wiring and supply	Must be known working.
Inline fuse or overcurrent protection	1 set	Matched to low-voltage circuit	Fault protection	Required before powered operation.
Emergency disconnect switch	1	Physical power cutoff reachable from operator position	Fast shutdown	Required.
Cable strain relief	1 set	Clips, tie points, or brackets	Prevents accidental pulling	Required near wet/electrical boundary.
Cable labels	1 set	Labels for supply, sensor, data, and ground/reference paths	Prevents wiring confusion	Required before first powered run.
Drip separation hardware	1 set	Physical elevation/routing to keep water from cables	Reduces electrical hazard	Required.
Electrical Rules

The first rig should use low-voltage, current-limited power only.

Do not use:

exposed mains wiring,
improvised high-voltage sources,
high-current output chasing,
unattended operation,
or wet-zone electrical clutter.

If water reaches electrical connections, stop the run.

Category 6: Water and Electrolyte Sensing
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Water thermometer	1	Water-compatible thermometer	Records water temperature	Required before run.
pH meter or pH strips	1	Basic pH measurement	Records water/electrolyte condition	Meter preferred for repeatability.
Conductivity or TDS meter	1	Water-quality meter	Records conductivity/TDS	Calibration solution preferred.
Calibration solution for pH meter	1 set	Matched to pH meter	Supports pH confidence	Required for quantitative pH claims.
Conductivity calibration solution	1	Matched to conductivity/TDS meter	Supports conductivity confidence	Required for quantitative conductivity claims.
Water sample labels	1 set	Labels for source, date, and run ID	Prevents sample confusion	Required.
Water record form	1	Printed or digital template	Evidence record	Required before accepted run.
Water Evidence Rule

No valid run should proceed to an accepted claim without a water record.

Unknown water means unknown interpretation.

Category 7: Thermal and Ambient Monitoring
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Ambient thermometer	1	Room temperature measurement	Supports repeatability	Required for run notes.
Ambient humidity measurement	1	Hygrometer or combined temp/humidity meter	Helps interpret condensation	Strongly preferred.
Electrolyzer surface temperature method	Optional	Non-contact or contact thermometer suitable for selected module	Detects abnormal heating	Useful safety check.
Gas path temperature probe	Optional	Low-range probe	Supports gas interpretation	Useful for stronger evidence.
Thermal input sensor	Optional	Temperature measurement for solar thermal branch	Future branch evidence	Not required for baseline.
Thermal Rules

Thermal assist is disabled by default for GH-BENCH-A0 baseline runs.

If thermal assist is ever used, thermal input must be measured and counted.

Do not claim efficiency improvement from heat unless heat input is included in the accounting.

Category 8: Data Logging and Evidence Capture
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Laptop, tablet, or local logging device	1	Local evidence capture	Records run data	Keep outside splash zone.
Time-synchronized clock source	1	Device timestamp or written timestamp standard	Aligns evidence	Required.
Manual run sheets	1 set	Paper backup forms	Prevents data loss	Required for first physical tests.
Camera or phone camera	1	Setup and anomaly photos	Visual record	Must not distract operator.
Data logger	Optional	Sensor and power logging	Improves traceability	Manual logging acceptable at A0.
Run ID labels	1 set	Labels for samples, photos, and forms	Prevents evidence mixing	Required.
Evidence storage folder convention	1	Digital folder structure	Organizes run bundle	Required before first run.
Evidence Capture Rule

A run without records is not evidence.

A failed run with complete records is more valuable than a successful-looking run with missing records.

Category 9: Operator Safety Hardware
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Eye protection	1 per operator	Safety glasses or goggles	Splash protection	Required.
Gloves	1 per operator	Compatible with water/electrolyte handling	Hand protection	Required if electrolyte is used.
Lab coat or protective apron	1 per operator	Splash protection	Strongly preferred.	
Spill kit	1	Appropriate to water/electrolyte selected	Spill response	Required before electrolyte use.
First-aid kit	1	Basic first-aid access	General safety	Required nearby.
Fire extinguisher appropriate to local guidance	1	Selected according to local electrical/chemical fire guidance	Emergency response	Operator must know location and limits.
Safety signage	1 set	Hydrogen test, no ignition sources, ventilation required	Area awareness	Required during testing.
Printed stop-condition checklist	1	Immediate abort criteria	Operator decision support	Required at bench.
Operator Safety Rule

No test is valid if the operator is forced to choose between saving data and staying safe.

If safety changes, stop the run.

Category 10: Physical Layout and Separation Hardware
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Nonflammable or chemically resistant tray	1	Bench containment	Controls spills and layout	Required.
Splash shield	1	Clear shield that does not trap gas	Operator splash separation	Must not create sealed volume.
Lab stand or rigid frame	1	Holds gas path and sensors	Repeatable layout	Required for A/B comparison.
Sensor rail or fixed mount	1	Repeatable sensor position	Reduces reading variability	Strongly preferred.
Tubing clips	1 set	Holds gas path	Prevents accidental movement	Required.
Cable clips	1 set	Holds power/data lines	Separates wet and electrical zones	Required.
Zone labels	1 set	Marks water, generation, gas handling, verification, and shutdown zones	Prevents confusion	Required.
Layout Rule

The bench should be divided into clear zones:
```
Zone 1: Water verification
Zone 2: Baseline generation
Zone 3: Gas-liquid handling
Zone 4: Gas verification
Zone 5: Power and shutdown
Zone 6: Evidence capture
```

Water and electrical routing should not cross casually.

Category 11: Sensor Calibration and Confidence Records
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Sensor inventory sheet	1	Lists every measurement device	Evidence provenance	Required.
Calibration log	1	Records calibration/bump-test state	Measurement confidence	Required for all sensors.
Sensor limitation sheet	1	Notes known limits and failure modes	Prevents overclaiming	Required.
Pre-run sensor check form	1	Confirms sensors are connected and plausible	Blocks bad runs	Required.
Post-run sensor check form	1	Confirms sensor state after test	Detects wetting or drift	Strongly preferred.
Calibration Rule

If a sensor is not calibrated or bump-tested, the repo must say so.

Do not pretend an uncalibrated sensor is quantitative evidence.

Category 12: Rejection and Stop-Support Materials
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Rejected-run form	1	Captures why a run failed	Preserves evidence	Required.
Anomaly log	1	Captures unexpected behavior	Supports review	Required.
Maintenance blocker sheet	1	Captures damaged tubing, expired sensor, unresolved leak, etc.	Prevents repeat unsafe runs	Required.
Red tag / do-not-use label	1 set	Marks unsafe components	Prevents accidental reuse	Strongly preferred.
Post-run inspection checklist	1	Confirms shutdown and hardware state	Preserves safety	Required.
Rejection Rule

A rejected run is not wasted.

It is a safety and learning artifact.

Minimum Acceptable Sensor/Safety Package

The minimum acceptable package for a physical baseline run includes:

Hydrogen-specific detector or sensor.
Independent area hydrogen awareness method where practical.
Water temperature measurement.
pH record method.
Conductivity or TDS record method.
DC voltage/current/power measurement.
Leak-check method.
Ventilation method.
Emergency power disconnect.
Eye protection.
Gloves if electrolyte is used.
Spill response materials.
Printed stop-condition checklist.
Run evidence forms.
Non-pressurized gas path.
Strong Review-Ready Sensor/Safety Package

A stronger package includes:

Calibratable hydrogen sensor.
Independent area hydrogen alarm.
Oxygen-side sensor.
Low-flow gas measurement method.
Gas temperature measurement.
Ambient temperature and humidity logging.
Data logger.
Independent power logger.
Calibration or bump-test records.
Fixed camera view or photo protocol.
Sensor mounting rail.
Post-run inspection forms.
Maintenance blocker labels.
Repeat-run evidence folders.
Hardware Not Allowed in GH-BENCH-A0

Do not include:

hydrogen storage tanks,
pressure vessels,
compressors,
sealed gas collection jars,
flame-test hardware,
high-voltage plasma supplies,
improvised ignition sources,
high-current optimization hardware,
undocumented catalysts,
mystery electrolytes,
unattended automation hardware,
or parts that make the gas path hard to inspect.
Pre-Purchase Questions

Before selecting exact models, answer:

Is the hydrogen detector actually hydrogen-specific?
Does it have a documented range?
Can it tolerate the expected humidity condition?
Can it be bump-tested or calibrated?
Does it require warmup?
Does it have known cross-sensitivities?
Can the gas path remain non-pressurized?
Can the sensor be mounted repeatably?
Can data be timestamped?
Can the operator shut down power immediately?
Can the run be stopped without touching the wet zone?
Can failed readings be preserved honestly?
Acceptance Criteria for This BOM

This sensor and safety BOM is acceptable when it supports:

hydrogen-specific detection,
leak awareness,
non-pressurized operation,
ventilation confirmation,
emergency shutdown,
water evidence,
electrical input evidence,
gas path evidence,
sensor confidence records,
run rejection,
and repeatable evidence bundles.
Failure Criteria for This BOM

This BOM is not acceptable if:

hydrogen detection is missing,
power measurement is missing,
ventilation is undefined,
emergency disconnect is missing,
gas path can become pressurized,
liquid can reach sensors easily,
water and electrical zones are mixed,
calibration state is ignored,
failed runs are not recorded,
or the selected hardware encourages unsupported claims.
First Physical Test Sensor Checklist

Before a first physical baseline run:

 Hydrogen detector selected and documented.
 Area hydrogen safety monitor selected or reason for absence documented.
 Oxygen-side observation method selected.
 Power meter selected.
 Water thermometer selected.
 pH method selected.
 Conductivity/TDS method selected.
 Leak-check method selected.
 Ventilation method selected.
 Emergency disconnect selected.
 Eye protection available.
 Gloves available if electrolyte is used.
 Spill kit available.
 Stop-condition checklist printed.
 Sensor log sheet ready.
 Evidence folder naming convention ready.
First Run Evidence Fields

Every physical run should record:
```
run_id
date_time
operator
location_type
ventilation_state
hydrogen_sensor_model
hydrogen_sensor_calibration_state
oxygen_sensor_model_or_observation_method
power_meter_model
water_temperature
water_ph
water_tds_or_conductivity
gas_path_description
leak_check_result
emergency_disconnect_confirmed
ppe_confirmed
stop_conditions_reviewed
run_duration_limit
branch_selected
sensor_anomalies
operator_notes
acceptance_status
```
Claim Boundary

With the minimum package, the repo may support only a bounded statement such as:
```
The system is efficient.
The system is green.
The system is scalable.
The system is safe for field deployment.
The system is commercially ready.
The system improves hydrogen output.
```

Those claims require additional calibrated data, repeatability, carbon accounting, and external review.

Final Rule

The sensor and safety package exists to make weak evidence obvious.

If a result cannot survive the sensor log, safety log, and gas-path record, it should not become a claim.
