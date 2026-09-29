# xNTTP Overview

## Model Workflow

An xNTTP run starts from an `.xrun` parameter file. The Landscape Model core validates these parameters, creates an
experiment workspace, and executes the configured components in sequence.

The standard workflow is:

1. Read landscape geometries and attributes from the selected scenario.
2. Create pesticide application events for the target fields and application years.
3. Calculate spatially explicit spray-drift exposure.
4. Optionally calculate threshold and dose-response effects for standard test species.
5. Pass the exposure grid to IBCgrass and simulate grassland community responses at the selected patch locations.

## Information Flow

| Stage | Main information produced | Used by |
| --- | --- | --- |
| Landscape scenario | Geometries, feature identifiers, land-cover types, extent, CRS | Application and exposure models |
| Pesticide application | Applied fields, dates, rates, areas, drift reductions | Spray-drift model |
| Spray drift | Daily exposure on a 1 m spatial grid | Effect models and IBCgrass |
| Standard effects | Threshold exceedance and endpoint-specific responses | Comparative analysis |
| IBCgrass | Plant-community simulation outcomes | IBCgrass result analysis |

The model configuration in `model/variant/mc.xml` is the authoritative definition of this component sequence and the
connections between component outputs and inputs.

## Runs and Results

Each run receives a simulation identifier (`SimID`). By default, logs and Monte Carlo workspaces are written below
`run/<SimID>`. The configured store preserves exchanged datasets, while component-specific processing directories hold
temporary and model-native files.

For a concise description of each model stage, see [Components](components.md).