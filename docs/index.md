# xNTTP Documentation

Welcome to the documentation for **xNTTP**, the xNonTargetTerrestrialPlants landscape model.

xNTTP links landscape geometry, pesticide application, spray-drift exposure, effect models, and the IBCgrass plant
community model in a reproducible component-based simulation. This initial documentation provides:

1. an introduction to the model's purpose and scope;
2. an overview of the xNTTP workflow and its main components;
3. an introduction to the IBCgrass integration and its parameterisation; and
4. a glossary of central terms.

## Documentation Quick Start

Install the documentation dependencies from the repository root:

```powershell
python -m pip install -r requirements-docs.txt
```

Start a local preview:

```powershell
python -m mkdocs serve
```

Build the static documentation:

```powershell
python -m mkdocs build --strict
```

## Recommended Reading Order

1. [Introduction](introduction.md)
2. [xNTTP Overview](xnttp/index.md)
3. [Components](xnttp/components.md)
4. [IBCgrass](ibcgrass/index.md)
5. [IBCgrass Parameterisation](ibcgrass/parameterisation.md)
6. [Glossary](glossary.md)