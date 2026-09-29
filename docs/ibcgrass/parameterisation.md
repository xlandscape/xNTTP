# IBCgrass Parameterisation

## Parameter Files

Users normally configure a run by copying `template.xrun`, changing its values, and saving the copy with an `.xrun`
extension. The schema at `model/variant/parameters.xsd` defines the required fields and basic value constraints.

The example below shows the structure of a parameter file:

```xml
<Parameters xmlns="urn:xNonTargetTerrestrialPlants">
  <Project>scenario/schematic-100x100</Project>
  <SimID>Example Run</SimID>
  <SimulateNonIbcEffects>false</SimulateNonIbcEffects>
  <SimulationFirstYear>2015</SimulationFirstYear>
  <SimulationLastYear>2018</SimulationLastYear>
  <ApplicationFirstYear>2016</ApplicationFirstYear>
  <ApplicationLastYear>2017</ApplicationLastYear>
  <ApplicationRate>1800</ApplicationRate>
  <InCropBuffer>0</InCropBuffer>
  <SprayDriftModel>90thRautmann</SprayDriftModel>
  <WindDirection>270</WindDirection>
  <PatchCenterX>5660687.5 5660737.5</PatchCenterX>
  <PatchCenterY>353915.5 353915.5</PatchCenterY>
  <PFT>$(_MODEL_DIR_)\..\ibc\pft.xlsx</PFT>
  <SeedsPerType>10</SeedsPerType>
</Parameters>
```

## User Parameters

| Parameter | Meaning | Constraint or unit |
| --- | --- | --- |
| `Project` | Scenario folder used by the run | Repository-relative path |
| `SimID` | Name of the run and output folder | At least 3 characters |
| `SimulateNonIbcEffects` | Enables the additional TerRQ and dose-response components | `true` or `false` |
| `SimulationFirstYear` | First year simulated by IBCgrass | 1900 to 2200 |
| `SimulationLastYear` | Last year simulated by IBCgrass | 1900 to 2200 |
| `ApplicationFirstYear` | First year containing pesticide applications | 1900 to 2200 |
| `ApplicationLastYear` | Last year containing pesticide applications | 1900 to 2200 |
| `ApplicationRate` | Nominal field application rate | Non-negative, `g/ha` |
| `InCropBuffer` | Untreated buffer inside the field boundary | Non-negative, `m` |
| `SprayDriftModel` | Exposure model selection | `XSprayDrift`, `90thRautmann`, or `AgDrift` |
| `WindDirection` | Direction used by the spray-drift model | -1 to 359 degrees |
| `PatchCenterX` | Easting of each IBCgrass patch centre | Space-separated coordinates in `m` |
| `PatchCenterY` | Northing of each IBCgrass patch centre | Space-separated coordinates in `m` |
| `PFT` | IBCgrass plant functional type workbook | Path to an `.xlsx` file |
| `SeedsPerType` | Annual seed input per PFT | Non-negative integer |

`PatchCenterX` and `PatchCenterY` must contain the same number of coordinates in corresponding order. Simulation years
should enclose the application period and must be ordered from first to last year.

## IBCgrass Defaults

Additional IBCgrass settings are currently model defaults in `model/variant/mc.xml`, rather than user parameters in
the `.xrun` file.

| Setting | Current default | Meaning |
| --- | ---: | --- |
| `CellNum` | 173 | IBCgrass grid size |
| `Tinit` | 1 year | Initialisation period |
| `MeanBRes` | 90 | Mean below-ground resources |
| `MeanARes` | 100 | Mean above-ground resources |
| `AreaEvent` | 0.1 | Area disturbed by trampling per year |
| `GrazProb` | 0.01 | Annual grazing probability |
| `Ncut` | 1 | Cutting events per year |
| `RecovDuration` | 1 year | Recovery duration |
| `EffectModel` | `dose-response` | Herbicide effect mode |
| `MCruns` | 3 | IBCgrass repetitions per patch |
| `NumberThreads` | 20 | Maximum parallel worker threads |

Changing these defaults affects every run using the model configuration. Promote a setting into `parameters.xsd` and
`template.xrun` when it should become a supported user-level parameter.

## Starting a Run

After saving the parameter file, drag it onto `__start__.bat`, or pass it from a command prompt:

```bat
__start__.bat "example.xrun"
```

Run logs and Monte Carlo workspaces are written below `run/<SimID>`.