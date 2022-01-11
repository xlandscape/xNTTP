## Table of Contents
* [About the project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


## About the project
xNonTargetTerrestrialPlants is a modular model that simulates processes at a landscape-scale and allows assessing 
potential effects of terrestrial non-target. Its main features are:
* A modular structure that couples existing expert models like and that allows to flexibly replace or add further 
  modules. 
* A unified and consistent view on the environmental state of the simulated landscape that is shared among modules and
  available to risk-assessment. 
* Data semantics that explicitly express values and their physical units at different spatial and temporal scales plus 
  the ability of transient data transformations according to the requirements of used models.
* Computational scaling that allows to conduct Monte Carlo runs in different sizes of landscapes, ranging from small
  schematic setups to real-world landscapes. 

### Built with
xNonTargetTerrestrialPlants is composed of the following building blocks: 
* The Landscape Model core that provides the base functionality for managing experiments and exchanging data in a 
  landscape-scale context. See `\model\core\README` for further details.  
* The AnalysisObserver that implements default assessments of simulations, including the output of maps, plots and 
  tables. See `\model\variant\AnalysisObserver\README` for further details.
* XDrift, a spray-drift model based on Rautmann drift values (
  [https://doi.org/10.1016/j.softx.2020.100610](https://doi.org/10.1016/j.softx.2020.100610)). See 
  `\model\variant\XSprayDrift\README` for further details.
* An exemplary schematic landscape scenario consisting of a 100 m x 100 m habitat next to a 100 m x 100 m field. See 
  `\scenario\schematic-100x100\README` for further details.
* Jupyter notebooks containing a series of exemplary analyses. See `\analysis` for further details.  


## Getting Started
xNonTargetTerrestrialPlants is portable and is tested to run on a range of hardware.

### Prerequisites
xNonTargetTerrestrialPlants requires a 64-bit Windows to run.

### Installation
$(installation_notes)


## Usage
1. Open the `template.xrun` in any text editor and modify the parameters for the simulation to your needs. The 
   `template.xrun` contains in-line documentation to assist you in deciding for valid parameter values.
2. Save the modified `template.xrun` under a different name in the same directory, using a `.xrun` extension.
3. Drag and drop the saved parameterization file onto the `__start__.bat`.
4. Check the console window occasionally for successful conclusion of the simulation or for errors. Logfiles can be
   found under `\run\<name-of-your-experiment>\log`.


## Roadmap
xNonTargetTerrestrialPlants is under continuous development. Future versions will include further and updated models. 
Usage of ontologies for semantic description of data are planned.


## Contributing
Contributions are welcome. Please contact the authors (see [Contact](#contact)).


## License
xNonTargetTerrestrialPlants is distributed under the CC0 License. See the according `LICENSE` files for more 
information.


## Contact
Thorsten Schad - thorsten.schad@bayer.com
Sascha Bub - sascha.bub@gmx.de


## Acknowledgements
See `README`s of individual building blocks for acknowledgements of these parts.
