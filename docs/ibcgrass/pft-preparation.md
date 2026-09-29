# PFT Preparation

## Purpose

`ibc/prepare_pft.py` creates a case-specific IBCgrass PFT workbook from:

- the ecological and life-history traits in the `ibc/pft.xlsx` template; and
- one tab-separated ecotox study file for each available effect endpoint.

The script sets `sens` to `random` for every PFT row and writes EC50 and slope intervals into the endpoint columns. The
xNTTP `IbcGrass` component later samples each interval independently when preparing an IBCgrass repetition.

The repository includes `ibc/pft_gly_case_study.xlsx`, generated from the biomass and survival studies described below.

## Biological Interpretation

The ecotox study and IBCgrass describe different kinds of entities:

- **Test species** are individual terrestrial non-target plant species exposed under standardized study conditions.
  Each usable species and endpoint yields one fitted dose-response curve with a paired EC50 and slope.
- **PFTs** are functional representations of grassland plants used by IBCgrass. Their traits describe growth,
  allocation, dispersal, clonality, and related ecological behavior; they are not taxonomic matches to the study
  species.

The available study therefore provides an empirical set of surrogate sensitivities, but it does not establish which
test-species response belongs to which PFT. Setting every PFT to `sens=random` expresses this missing correspondence.
It means that no PFT is assumed a priori to behave like a particular test species, and the transfer uncertainty is
propagated across IBCgrass repetitions.

This randomization is endpoint-specific. A Vegetative Vigour study can directly inform established-plant biomass and
survival, while seedling biomass, establishment, sterility, and seed number require evidence from corresponding study
endpoints. An endpoint without supporting evidence is set to zero rather than inferred from another endpoint.

!!! important "Random assignment versus the implemented sampler"
    Conceptually, `random` stands for an unknown assignment of PFTs to test-species dose-response functions. The
    current xNTTP implementation approximates that assignment by sampling EC50 and slope **independently** from
    continuous endpoint-specific intervals. It does not select one intact observed test-species EC50/slope pair.

    Consequently, a realized curve can combine an EC50 and slope that did not occur together in the study. Biomass
    and survival are also sampled independently, so a PFT is not assigned a persistent surrogate test-species identity
    across endpoints. Literal random selection of complete observed curves would require a different workbook/runtime
    representation that preserves the paired parameters and endpoint-specific species identities.

## Input Files

### PFT Template

By default, the script uses `ibc/pft.xlsx`. It preserves all worksheets, PFT rows, ecological traits, formatting, and
workbook structure. The template must contain the standard 43-column xNTTP IBCgrass schema.

### Ecotox Dose-Response Files

Each endpoint file must be tab-separated and end its header with `Spec`, `EC50`, and `b`. An optional leading row-name
column is accepted, as in the case-study files:

```text
"Spec"  "EC50"  "b"
"1"     "Spec1" "29.5"   "2.710644292185129"
"2"     "Spec2" "117.56" "2.6228197689925734"
...
"11"    "mean"  "161.545" "2.90478770343618"
"12"    "sd"    "185.935339970647" "0.807099376419697"
```

The script reads the species rows and recomputes summary statistics. Rows named `mean`, `sd`, or
`standard deviation` are ignored. EC50 and slope values must be finite and positive, and each file must contain at
least two species-level functions.

Supported endpoint names and workbook destinations are:

| Endpoint argument | EC50 column | Slope column |
| --- | --- | --- |
| `biomass` | `EC50_biomass` | `slope_biomass` |
| `seedling-biomass` | `EC50_SEbiomass` | `slope_SEbiomass` |
| `survival` | `EC50_survival` | `slope_survival` |
| `establishment` | `EC50_establishment` | `slope_establishment` |
| `sterility` | `EC50_sterility` | `slope_sterility` |
| `seed-number` | `EC50_seednumber` | `slope_seednumber` |

## Generate the GLY Case-Study Workbook

Run the script from the xNTTP repository root with the bundled Python interpreter, which already provides `openpyxl`:

```powershell
$python = ".\model\core\bin\python-3.9.7-amd64\python.exe"
$ecotox = "C:\LocalWork\IBCgrassGUI-Landwerk\GLY_CaseStudy\IBCgrass_input_preparation\ecotox"

& $python .\ibc\prepare_pft.py `
  --output .\ibc\pft_gly_case_study.xlsx `
  --endpoint "biomass=$ecotox\EC50andslope_Biomass.txt" `
  --endpoint "survival=$ecotox\EC50andslope_Survival.txt" `
  --force
```

The template defaults to `ibc/pft.xlsx`. Use `--template <file>` to select another compatible workbook.

## From Test-Species Curves to Intervals

The default `mean-sd` method follows the reference IBCgrass GUI workflow. For each parameter independently, it uses:

```text
lower = max(0, species mean - sample standard deviation)
upper = species mean + sample standard deviation
```

The GLY studies produce:

| Model endpoint | Study curves | EC50 interval | Slope interval |
| --- | ---: | --- | --- |
| Established-plant biomass | 10 | `[0;347.48034]` | `[2.097688;3.711887]` |
| Established-plant survival | 8 | `[198.126477;520.428523]` | `[5.599892;17.023382]` |

These are parameter-sampling bounds, not confidence intervals and not fitted dose-response curves themselves. For an
application rate $r$, IBCgrass calculates the affected fraction from a sampled pair as:

$$
\operatorname{effect}(r) = \frac{r^b}{EC50^b + r^b}
$$

A lower EC50 represents a more sensitive response because the same application rate produces a larger effect. The
slope $b$ controls how abruptly the response changes around EC50.

To use the full observed range instead, add `--interval-method range`. This produces intervals from the minimum and
maximum species estimates, excluding summary rows. It remains a continuous independent-parameter sampler; it does not
change the workflow to discrete selection of observed curves.

Use `--precision <n>` to change the default maximum of six decimal places. Trailing zeroes are omitted.

## Workbook Update Rules

For every non-empty PFT row on every worksheet, the script:

1. sets `sens` to `random`;
2. clears all six EC50/slope endpoint pairs to numeric zero; and
3. writes intervals only for endpoints supplied with `--endpoint`.

Clearing unmapped endpoints is deliberate: it prevents parameters left in the template from introducing effects that
are unsupported by the case-specific ecotox studies. In the GLY workbook, biomass and survival are populated while
seedling biomass, establishment, sterility, and seed number remain zero.

Every PFT receives the same endpoint intervals because there is no PFT-specific ecotoxicological evidence. During PFT
text-file preparation, each parameter is sampled separately for each PFT and IBCgrass repetition. Thus variability
between PFT responses in this setup represents uncertain sensitivity assignment, not measured differences among the
grassland PFTs.

The output must differ from the template. Existing output is protected unless `--force` is supplied. The workbook is
written through a temporary file and atomically replaces the destination after successful preparation.

## Use in xNTTP

Point the `PFT` entry of the run's `.xrun` file to the generated workbook:

```xml
<PFT>$(_MODEL_DIR_)\..\ibc\pft_gly_case_study.xlsx</PFT>
```

No generated text file needs manual preparation. During the run, the `IbcGrass` component reads this workbook, samples
the intervals separately for each repetition, converts `sens=random` to a numeric runtime value, and creates the
immediate PFT text files consumed by `IBCgrassGUI.exe`.

The numeric conversion of `sens` is a file-format compatibility step. Dose-response behavior is determined by the
sampled endpoint EC50 and slope values; the word `random` itself is not consumed by `IBCgrassGUI.exe`.

The current component uses Python's unseeded random-number generator for these draws. Repeating an otherwise identical
xNTTP run does not guarantee the same PFT dose-response assignments. Preserve the generated PFT text files with study
outputs when exact reconstruction of a realization is required.

## Command Reference

```text
prepare_pft.py --output FILE --endpoint ENDPOINT=FILE [--endpoint ...]
               [--template FILE] [--interval-method mean-sd|range]
               [--precision N] [--force]
```

The command exits without creating or replacing the destination if an endpoint is unknown, an input file is invalid,
a required workbook column is missing, or the destination already exists without `--force`.