## Installation

To install Fenv, simply run the following command:

```sh
pip install fenv
```

## Usage

Fenv makes it easy to get started with a new Python project by providing an all-in-one solution. Here's how to use it:

## Create a new project with virtualenv and basic files:

```sh
fenv new <project_folder>
```

## Activate the virtual environment:

### for windows

```
cd project_folder
source env/bin/activate
```

### for linux

```
cd project_folder
source env/bin/activate
```

# Command for windows only

## Install packages

```
fenv install <package_name>
```

Install the package and add it to requirements.txt If the package name is omitted, the message `Maybe you forgot to put the name of the package to install? for example fenv install <package_name>` is displayed.

## Uninstall packages

```
fenv uninstall <package_name>
```

Uninstall the package and delete it from requirements.txt

## Update requirements.txt

```
fenv update <package_name>
```

Update all packages to a file. requirements.txt

## Create virtualenv only

```
fenv onlyenv
```

Create a virtualenv with a custom name or an optional 2 autoname, then create a file. settings.json for vscode does not generate additional base files