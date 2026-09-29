# Introduction

## What xNTTP Is

xNTTP, short for **xNonTargetTerrestrialPlants**, is a modular landscape model for simulating the exposure and effects
of plant-protection products on non-target terrestrial plants. It combines spatial landscape information with models
for pesticide use, spray drift, ecological effects, and plant-community dynamics.

The model is built on the Landscape Model core. Components exchange values together with semantic information such as
data type, physical unit, and spatial or temporal scale. This allows specialist models to be connected in a common,
reproducible simulation workflow.

## Purpose

xNTTP supports investigations of how pesticide applications in cropped fields can affect plants and plant communities
outside the treated area. Depending on the run configuration, effects can be evaluated with standard dose-response
endpoints, with IBCgrass community simulations, or with both approaches.

## Main Capabilities

- component-based simulation of landscape-scale processes;
- spatially explicit calculation of spray-drift exposure;
- optional threshold and dose-response effect calculations for standard test species;
- integration of IBCgrass for individual-based grassland community simulation;
- Monte Carlo execution and structured storage of intermediate and final results; and
- analysis notebooks for exploring model outcomes.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `model/core` | Landscape Model framework and reusable components |
| `model/variant` | xNTTP-specific configuration and integrations |
| `scenario` | Landscape, weather, and related scenario data |
| `ibc` | IBCgrass plant functional type input data |
| `analysis` | Example analysis notebooks |
| `run` | Simulation workspaces and results |
| `template.xrun` | Example user parameterisation |

Continue with the [xNTTP Overview](xnttp/index.md) for the model workflow.