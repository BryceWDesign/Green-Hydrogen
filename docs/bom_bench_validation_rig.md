# BOM: Bench Validation Rig

## Purpose

This bill of materials defines the supplier-neutral hardware classes needed for the first Green-Hydrogen bench validation rig.

The goal is not to build a high-output hydrogen system.

The goal is to build a conservative, non-pressurized, instrumented bench setup that can support measured, reviewable proof-of-concept testing.

## First Rig Name

```
GH-BENCH-A0
```

Build Boundary

GH-BENCH-A0 is:

bench-scale,
non-pressurized,
supervised,
ventilated,
low-output,
baseline-first,
measurement-first,
and designed for evidence capture.

GH-BENCH-A0 is not:

a pressure system,
a hydrogen storage system,
a commercial electrolyzer,
a certified gas appliance,
an unattended system,
a field deployment,
or a green-hydrogen performance claim.
BOM Philosophy

Every component in the first build should support at least one of these jobs:

Make the setup safer.
Make the measurement clearer.
Make the evidence easier to audit.
Make failure easier to detect.
Make the test easier to repeat.
Prevent unsupported claims.

Do not buy parts merely because they look advanced.

BOM Readiness Status
BOM Area	Current Status	Notes
Bench and containment	Supplier-neutral complete	Exact vendor not locked.
Water verification	Supplier-neutral complete	Needs chosen meter models.
Baseline electrolysis reference	Supplier-neutral partial	Prefer certified educational/lab module.
Non-pressurized gas handling	Supplier-neutral partial	Must be reviewed before physical build.
Gas verification	Supplier-neutral partial	Exact hydrogen sensor model still required.
Electrical measurement	Supplier-neutral complete	Use low-voltage current-limited supply.
Safety hardware	Supplier-neutral complete	Must be chosen before test.
Data logging	Supplier-neutral complete	Can start manual, then automate.
Gankyil-A prototype materials	Supplier-neutral partial	Geometry still needs final lock.
Assembly hardware	Supplier-neutral complete	Standard non-sparking and corrosion-aware selection preferred.
Critical Safety Procurement Rule

Do not substitute unknown parts into the gas path.

The gas path must remain:

non-pressurized,
visible where practical,
leak-checked,
short,
inspectable,
compatible with water vapor,
compatible with hydrogen exposure,
and easy to disconnect after shutdown.
Category 1: Bench, Mounting, and Work Area
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Nonflammable bench surface or tray	1	Chemically resistant tray or nonflammable work surface, minimum about 24 in x 18 in	Creates controlled work area	Must contain minor spills and keep components organized.
Secondary containment tray	1	Shallow tray compatible with water/electrolyte exposure	Captures leaks and spills	Must fit under electrolysis and separation area.
Clear splash shield	1	Transparent bench shield or panel	Separates operator from splash zone	Should not trap gas or create sealed volume.
Lab stand or rigid frame	1	Adjustable stand, rail, or frame	Holds tubing, sensors, separator, and Gankyil-A chamber	Must prevent tipping or pulling.
Clamp set	1 set	Adjustable clamps compatible with tubing and small chambers	Secures gas path and containers	Avoid crushing tubing.
Cable/tubing management clips	1 set	Adhesive or mechanical clips	Prevents cable/tubing movement	Must keep electrical and wet zones separated.
Label tape	1 roll	Water-resistant labels	Labels water, tubing direction, sensors, and run IDs	Required for evidence clarity.
Absorbent pads	1 pack	Lab/bench absorbent pads	Spill response	Must not be placed where they block ventilation.
Small parts tray	1	Divided tray	Keeps fittings, caps, and adapters organized	Helps prevent accidental substitution.
Category 2: Water Verification Station
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Clean water sample containers	3-6	Clear, sealable, labeled containers	Holds water samples and repeats	Must be clean and labeled.
Measuring cylinder or graduated container	1	Appropriate small-volume graduated container	Measures water input volume	Must be readable and stable.
Digital thermometer	1	Water-compatible thermometer	Records water temperature	Must be checked against ambient reasonableness.
pH meter or pH test strips	1	Basic water pH measurement	Records pH before run	Meter preferred; strips acceptable for early screen.
TDS or conductivity meter	1	Handheld water-quality meter	Records conductivity/TDS	Calibration solution preferred.
Turbidity/clarity reference	1	Simple visual clarity card or turbidity tube	Records visible water condition	Early version may be qualitative.
Calibration solution for pH	1 set	Standard pH buffers if using meter	Supports pH confidence	Required if making quantitative pH claims.
Conductivity calibration solution	1	Standard solution matched to meter	Supports TDS/conductivity confidence	Required if making quantitative conductivity claims.
Disposable pipettes or transfer tools	1 pack	Clean transfer tools	Prevents contamination	Use only for water/electrolyte handling.
Water record sheets or digital form	1	Printed or digital template	Captures water evidence	Must be completed before valid run.
Category 3: Baseline Electrolysis Reference
Preferred Procurement Path

For GH-BENCH-A0, the baseline hydrogen source should be a commercially available educational or lab demonstration electrolysis module designed for low-volume hydrogen generation.

This avoids unnecessary custom electrochemical risk during the first proof stage.

Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Low-output electrolysis reference module	1	Commercial educational/lab PEM-style or equivalent low-volume hydrogen generator	Provides conservative baseline gas generation	Must be used according to its documentation and never pressurized beyond intended use.
Compatible electrolyte, if required	As required	Only as specified by selected module	Supports operation if module requires electrolyte	Do not improvise electrolyte chemistry.
Replacement membrane/electrode kit	Optional	Matched to selected module	Maintenance and repeatability	Record any replacement before run.
Cell mounting base	1	Nonconductive, stable mount	Prevents tipping and strain	Must isolate wet zone from electronics.
Drip tray under cell	1	Chemically compatible tray	Captures water/electrolyte leaks	Must be inspected after run.
Short connection leads	1 set	Properly rated for selected current	Power connection	Must be strain-relieved.
Inline fuse or current protection	1	Matched to selected low-voltage supply	Electrical fault protection	Required before powered runs.
Baseline Electrolysis Restrictions

Do not use:

pressure storage,
improvised sealed jars,
flame verification,
high-current pushing,
unknown electrode materials,
undocumented electrolyte blends,
or unattended operation.
Category 4: Non-Pressurized Gas Handling
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Hydrogen-compatible flexible tubing	As needed	Short tubing length, compatible with water vapor and hydrogen exposure	Routes gas from generation to verification path	Must be non-pressurized and inspected.
Barbed or compression fittings	As needed	Compatible with selected tubing and low-volume non-pressurized gas path	Connects modules	Must be leak-checked.
One-way check valve	1-2	Low-cracking-pressure gas-compatible valve	Helps prevent backflow where appropriate	Must not create unsafe pressure buildup.
Liquid trap / knock-out bottle	1	Transparent non-pressurized trap	Captures liquid carryover	Must vent safely and not store gas.
Baseline separator path	1	Simple visible gas-liquid separation path	A-side comparison for Gankyil-A	Must be documented and repeatable.
Gankyil-A removable chamber	1	Transparent or inspectable passive phase-management chamber	B-side comparison	Must be removable and non-pressurized.
Vent path or safe exhaust interface	1	Open-to-safe-vent path appropriate for location	Prevents accumulation	Must not terminate near ignition source.
Tubing caps/plugs for storage only	As needed	For dry storage after shutdown	Keeps dust out after disassembly	Never use to seal gas during operation.
Leak-check solution or method	1	Compatible leak-check method for selected fittings	Detects leaks	Must not contaminate sensors.
Gas Handling Boundary

The gas path is for observation and measurement only.

It is not for storage.

Category 5: Gas Verification
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Hydrogen detector or sensor	1 minimum	Hydrogen-appropriate sensor/detector with known range and documentation	Detects hydrogen presence	Exact model must be logged.
Hydrogen sensor calibration or bump-test method	1	Vendor-supported calibration/bump-test approach where practical	Improves confidence	Required before quantitative claims.
Oxygen sensor or oxygen-side detector	1	Oxygen measurement or oxygen-side observation tool	Watches O2 side and crossover concerns	Required for stronger evidence.
Gas flow meter or volume measurement method	1	Low-flow gas measurement compatible with wet gas or protected from water	Estimates output rate	Must not create unsafe restriction.
Humidity/water trap before sensor	1	Compatible trap or demister	Protects sensors from liquid carryover	Must be inspected.
Gas temperature sensor	Optional	Low-cost temperature probe	Records gas path temperature	Useful for repeatability.
Sensor mounting bracket	1 set	Rigid mount near verification zone	Stabilizes readings	Must prevent movement between A/B tests.
Calibration log sheet	1	Printed or digital form	Records sensor state	Required for evidence bundle.
Gas Verification Rule

Visible bubbles are not enough.

A valid hydrogen claim needs hydrogen-specific measurement.

Category 6: Electrical Input and Power Measurement
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Current-limited DC bench supply	1	Low-voltage, current-limited supply appropriate for selected electrolysis module	Provides controlled input	Must have readable voltage/current display.
Inline power meter or data logger	1	DC watt-hour capable meter or logger	Records energy input	Required for any energy claim.
Multimeter	1	Basic digital multimeter	Cross-checks voltage/current	Should be known working.
Inline fuse holder and fuses	1 set	Matched to circuit limits	Fault protection	Required.
Emergency power switch	1	Accessible switch or disconnect	Manual shutdown	Must be reachable without crossing wet zone.
Insulated leads	1 set	Rated leads with secure connectors	Connects supply to module	Must be strain-relieved.
Cable labels	1 set	Labels for power, sensor, and ground paths	Prevents confusion	Required before first powered run.
Nonconductive cable clips	1 set	Cable routing	Keeps power away from water	Required for tidy bench.
Electrical Boundary

Use low-voltage, current-limited power only for the first validation rig.

Do not use mains-exposed wiring, improvised high-voltage sources, or unattended power.

Category 7: Renewable Traceability and Solar Input

For first baseline testing, renewable traceability can be documented even if the run uses a bench supply.

Solar input does not need to be active in the first run.

Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Solar panel, small bench scale	Optional	Small DC panel appropriate for later controlled tests	Future renewable input test	Not required for baseline.
Solar charge controller or MPPT module	Optional	Matched to panel and battery if used	Records solar/battery pathway	Must be documented.
Battery pack with known chemistry	Optional	Properly protected battery system	Future stored-solar test	Must include protection and source record.
Solar irradiance note method	Optional	Simple irradiance meter or weather/log note	Documents solar condition	Useful for later tests.
Renewable source log	1	Digital or printed form	Records energy source	Required for green claim.
Renewable Claim Rule

Hydrogen is not green by default.

The run must record where the energy came from.

Category 8: Safety Hardware
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
General ventilation method	1	Location-appropriate ventilation suitable for hydrogen work	Prevents accumulation	Must be confirmed before run.
Hydrogen alarm/detector for area safety	1	Area monitor separate from process sensor if possible	Safety monitoring	Strongly preferred.
Emergency stop / disconnect	1	Physical disconnect accessible from operator position	Stops power quickly	Required.
Fire extinguisher appropriate to local guidance	1	Selected according to local electrical/chemical fire guidance	Emergency response	Operator must know location and limits.
Eye protection	1 per operator	Safety glasses or goggles	Splash protection	Required.
Gloves	1 per operator	Compatible with water/electrolyte handling	Hand protection	Required if electrolyte is used.
Spill kit	1	Appropriate to selected electrolyte/water handling	Spill response	Required before electrolyte use.
Safety signage	1 set	"No ignition sources", "Hydrogen test", "Ventilation required"	Area awareness	Useful even for bench work.
First-aid kit	1	Basic kit	General safety	Required in work area.
Run-abort checklist	1	Printed stop-condition checklist	Fast decision support	Required near bench.
Category 9: Data Logging and Evidence Capture
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Laptop or tablet	1	Local data capture and run forms	Records evidence	Must be away from wet zone.
USB data logger or microcontroller logger	Optional	Logs sensors if supported	Improves repeatability	Manual logging acceptable at A0.
Camera or phone camera	1	Photos of setup and run state	Visual evidence	Avoid unsafe positioning.
Timestamp source	1	Device clock or logging timestamp	Aligns records	Required for run bundle.
Printed run sheets	1 set	Backup manual records	Prevents data loss	Useful during first tests.
File naming convention	1	Run ID format	Keeps evidence organized	Required before first run.
Category 10: Gankyil-A Prototype Materials

The Gankyil-A chamber is a passive phase-management test article.

It must be inspectable and removable.

Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Transparent chamber body	1	Clear, chemically compatible, non-pressurized chamber	Allows visual observation	Must not be used as pressure vessel.
Internal guide vanes or inserts	1 set	Removable passive geometry inserts	Creates Gankyil-style pathing	Must be cleanable.
Inlet fitting	1	Compatible with tubing	Gas/liquid entry	Must be leak-checked.
Outlet fitting	1	Compatible with tubing	Gas exit	Must not restrict venting.
Drain or liquid-return point	Optional	Non-pressurized drain feature	Removes condensate	Must not create sealed volume.
Mounting bracket	1	Holds chamber vertical or defined orientation	Repeatable A/B setup	Orientation must be recorded.
Visual scale marking	1	External ruler/marking	Observes liquid level/carryover	Do not mark inside gas path.
Gankyil-A Boundary

Gankyil-A is not a hydrogen generator.

It is a phase-management comparison article.

Category 11: Assembly Consumables
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
PTFE tape or compatible thread sealant	As needed	Only if appropriate for selected fittings	Helps seal threaded joints	Must not contaminate gas sensor path.
Zip ties or hook-and-loop straps	As needed	Cable/tubing organization	Prevents movement	Do not pinch tubing.
Distilled or documented water	As needed	Known water source	Baseline water input	Must be recorded.
Cleaning wipes	1 pack	Lint-free, compatible with bench materials	Cleans exterior surfaces	Do not contaminate sensors.
Disposable gloves	1 box	General handling	Prevents contamination	Required for clean assembly.
Small waste container	1	For used wipes/consumables	Housekeeping	Follow local disposal rules.
Category 12: Documentation and Review Materials
Item	Qty	Supplier-Neutral Specification	Purpose	Acceptance Notes
Printed preflight checklist	1	Safety gate checklist	Blocks unsafe run	Must be signed or timestamped.
Printed water record	1	Water verification form	Documents input water	Required.
Printed power record	1	Voltage/current/duration form	Documents energy	Required.
Printed gas record	1	Hydrogen/oxygen/gas path form	Documents gas evidence	Required.
Printed anomaly sheet	1	Captures weird behavior	Preserves failures	Required.
Printed acceptance sheet	1	Accepted/rejected/inconclusive decision	Controls claims	Required.
Minimum BOM for Dry Software/Evidence Run

Before buying any hardware, the repo can run a dry validation using:

Item	Qty	Purpose
Example run intent JSON	1	Simulates operator intent.
Safety preflight script	1	Checks whether run should be blocked.
Evidence bundle script	1	Builds reviewable output.
Acceptance script	1	Produces claim decision.
Example rejected run	1	Confirms missing evidence is blocked.
Minimum BOM for Physical Baseline Run

A minimal physical baseline run requires:

Low-output commercial electrolysis reference module.
Current-limited low-voltage power supply.
Inline power measurement.
Water verification tools.
Non-pressurized gas path.
Hydrogen detector or hydrogen measurement method.
Leak-check method.
Ventilation method.
Emergency disconnect.
Eye protection and spill response.
Evidence forms.
Minimum BOM for Stronger Reviewable Baseline

A stronger baseline package requires:

Calibrated hydrogen sensor.
Oxygen-side sensor.
Gas flow or volume measurement.
Data logging.
Area hydrogen alarm.
Repeat water-quality records.
Repeat power records.
Repeat run bundles.
Calibration logs.
Photo documentation.
Minimum BOM for Gankyil-A A/B Test

A proper Gankyil-A comparison requires:

Baseline separator path.
Removable Gankyil-A chamber.
Same electrolysis reference module.
Same water source.
Same electrical input range.
Same sensor position.
Same run duration.
Liquid carryover observation method.
Gas path stability record.
Repeat comparison runs.
Procurement Priority

Recommended purchase/build order:

Safety hardware.
Water verification tools.
Electrical measurement tools.
Low-output electrolysis reference module.
Gas verification tools.
Non-pressurized gas handling parts.
Data logging support.
Baseline separator path.
Gankyil-A chamber materials.
Optional solar traceability hardware.

Do not buy advanced branch hardware first.

Parts That Should Not Be Purchased for A0

Avoid for GH-BENCH-A0:

hydrogen compression hardware,
hydrogen storage tanks,
pressure vessels,
high-voltage plasma supplies,
flame-test tools,
undocumented catalysts,
unknown electrolytes,
high-temperature heaters,
sealed reaction vessels,
unattended automation kits,
or any part marketed with unsupported miracle-efficiency claims.
BOM Review Checklist

Before physical assembly, confirm:

 All gas-path parts are compatible with hydrogen exposure.
 Gas path is non-pressurized.
 No part is intended for hydrogen storage.
 Water and electrical zones are separated.
 Emergency disconnect is present.
 Ventilation method is identified.
 Hydrogen detection method is selected.
 Leak-check method is selected.
 Power measurement method is selected.
 Water verification method is selected.
 Evidence forms are ready.
 Operator understands stop conditions.
BOM Acceptance Criteria

The BOM is acceptable for the first bench plan when it supports:

Baseline hydrogen detection.
Water input evidence.
Electrical input evidence.
Gas path evidence.
Safety preflight.
Leak-check record.
Non-pressurized operation.
Evidence bundle creation.
Rejected-run handling.
Gankyil-A A/B comparison later.
BOM Failure Criteria

The BOM is not acceptable if it includes:

pressure storage,
missing hydrogen detection,
missing emergency disconnect,
missing ventilation method,
missing water verification,
missing power measurement,
undocumented gas path,
unreviewed advanced branch,
improvised high-voltage hardware,
or any hardware that makes the first run harder to inspect.
Current BOM Lock Status

The BOM is supplier-neutral and suitable for planning.

It is not yet locked for procurement.

Exact models still need to be selected for:

hydrogen sensor,
oxygen sensor,
electrolysis reference module,
flow/volume measurement device,
DC power meter,
ventilation setup,
and Gankyil-A chamber material.
Final BOM Rule

The first rig should be built around evidence, not ambition.

If a part does not improve safety, measurement, repeatability, or evidence quality, it probably does not belong in GH-BENCH-A0.
