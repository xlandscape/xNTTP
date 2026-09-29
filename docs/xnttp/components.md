# Components

xNTTP is assembled from components supplied by the Landscape Model core and from model-specific integrations. The
following list groups repeated dose-response instances into one component type.

## Main Components

### LandscapeScenario

Reads the selected scenario package and provides landscape geometries, identifiers, land-cover classes, coordinate
reference information, and spatial extent. These values establish the shared spatial context for the run.

### PpmCalendar

Creates pesticide application events for eligible fields. It provides application dates, rates, treated areas, and
technology drift reductions to the exposure model.

### SprayDrift

Calculates pesticide deposition outside treated fields. It combines landscape geometry and application events with the
selected drift model, wind direction, buffers, and filtering settings. Its principal output is a time-dependent
exposure grid in `g/ha`.

### TerRQ

Compares exposure with a configured threshold. This component is part of the optional non-IBC effect workflow and is
enabled through `SimulateNonIbcEffects`.

### DoseResponse

Transforms exposure into endpoint-specific responses using slope and EC50 parameters. The model configuration contains
instances for vegetative-vigour and seedling-emergence endpoints of several standard test species. These instances are
also controlled by `SimulateNonIbcEffects`.

### IbcGrass

Connects xNTTP to the IBCgrass simulation engine. It selects exposure at configured patch centres, prepares IBCgrass
input files, runs the requested repetitions, and returns model-native outcomes in its processing workspace.

## Supporting Infrastructure

The Landscape Model core also provides observers for console and log output and an `X3dfStore` for values exchanged
between components. These services support execution and traceability but do not represent ecological processes.

See [IBCgrass Intro](../ibcgrass/index.md) for more about the community model integration.