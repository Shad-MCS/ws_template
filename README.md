# WS Cookiecutter Template

_A minimalistic project structure for Python packages and modules._

## Installation

This package requires Python 3.8+ and [Cookiecutter](https://www.cookiecutter.io/). Since we already work with Conda for environment management, I recommend creating a standalone environment for cookiecutter templates:

```bash
# Create an environment for cookiecutter
conda create -n cookiecutter_env python=3

conda activate cookiecutter_env
```

Then install cookiecutter using pip (which is the recommended way):

```bash
pip install cookiecutter
```

After this, please ensure that you have the most recent cookiecutter version from PyPI, which, at the time of this writing, is 2.6.0. You can check it by running

```bash
cookiecutter -V
```

## Starting a new project

To start a new project, run:

```bash
cookiecutter https://github.com/Shad-MCS/ws_template.git
```

Running this will prompt you to fill a number of fields that will populate the template. Values in brackets are defaults (see example below):

```
[1/8] author_name (Naushad AL Velgy):
                    ^
        this is a  / 
        default value
```

This is the current list of fields it requests:

| Field | Default | Description |
|:------|:--------|:------------|
|`author_name`|Naushad AL Velgy|Your name|
|`author_email`|shad@mcsaatchi.com|Your email|
|`github_username`|Shad-MCS|Your MCS GH username|
|`project_name`|Project_Name|The name of this project. This is currently only used to populate other fields (see below).|
|`repo_name`|project_name|The name of the github repository where the codebase will be hosted. Defaults to a lower case version of `project_name`.|
|`module_name`|project_name|The name of the module we are building (```from module_name import function```).|
|`project_short_description`|(It's too long to put here)|A simple description for this module.|
|`version`|0.0.1|The current version of this module. Defaults to version 0.0.1 (see the section on versioning for more).|

### The resulting directory structure

The directory structure of your new project will look something this:

```
├── README.md          <- The top-level README for developers using this project.
├── data               <- This should house data for testing.
│   ├── external       <- Data from third party sources.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── notebooks          <- Jupyter notebooks. Naming convention is the date in the
│                         form YYYYMMDD, the purpose of the notebook, then the creator's
|                         initials, separated by "_", e.g. 20240531_DataExploration_NV.ipynb.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── AUTHORS.rst        <- Who to contact if/when stuff breaks!
│
├── MANIFEST.in        <- Allows for more granular control of what files are included on our package.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, 
│                         e.g. generated with `pip freeze > requirements.txt`
│
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
    ├── common.py               <- Holds all functionality that is used across 
    │                              multiple parts of the code (like common 
    │                              classes).
    │
    ├── config.py               <- Functionality for loading configurations.
    │
    └── config.yaml             <- Configurations used for this module.
```

## Contributing

If you have a suggestion for improving this template, please get in touch!

## TO DO

 * Add a testing suite for the template installation.

### Further resources

This minimal template has been inspired by the following cookiecutter templates:

* `https://github.com/audreyfeldroy/cookiecutter-pypackage`: A cookiecutter template for a Python package.
* `https://github.com/drivendataorg/cookiecutter-data-science`: "A logical, reasonably standardized but flexible project structure for doing and sharing data science work."

#### A note on MANIFEST files

See this [link](https://stackoverflow.com/q/24727709) for guidelines on MANIFEST.in files.

#### A note on versioning

There are 2 easy to understand versioning systems that I recommend using either (calendar versioning)[https://calver.org/] or (semantic versioning)[https://semver.org/]. See this (link)[https://packaging.python.org/en/latest/discussions/versioning/] for a more detailed discussion on both in the Python ecosystem.

#### Changelog

 * 0.0.2 (current) - Added README and removed some vestigial files that should not be part of the template.
 * 0.0.1 - Initial upload.