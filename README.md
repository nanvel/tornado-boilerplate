# Tornado project template

## Features

### Requirements

Requirements per environment.

### Modules

Split project into reusable modules.

### URLS management

Each module could have its own urls file.

### Settings

Settings load sequence:

- execution args
- environment variables
- defaults

Settings definitions must be located in the top of the module ```__init__.py``` file they belongs to.

### Custom HTTP Error exception

Allows to return json contains error message and code.

### Prefilled app.py

Creates application.

### Documentation

Creates docs folder.

### Signals

QT like observer pattern implementation.

## Usage

### Virtual environment

```bash
virtualenv .env --no-site-packages -p /usr/local/bin/python3.5
source .env/bin/activate
pip install -r requirements/development.txt
```

## Conventions

### Imports

Use relative imports for imports from current module.

Imports [should be](https://www.python.org/dev/peps/pep-0008/#imports) grouped in the following order:

- standard library imports
- related third party imports
- local application/library specific imports

You should put a blank line between each group of imports.

Use ```__all__``` to specify which objects are for usage outside. Than use wildcard imports in ```__init__.py```. 

## Tests

```bash
python -m unittest project.module
```
