## Installation

To install Fenv, simply run the following command:

```sh
pip install fenv
```

## Usage

Fenv makes it easy to get started with a new Python project by providing an all-in-one solution. Here's how to use it:

## Create a new project folder:

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

## Uninstall packages

```
fenv update <package_name>
```

Update the package all to requirements.txt

## Create virtualenv only

```
fenv onlyenv
```

Create virtualenv only with 2 choice custom name and auto name then create file settings.json for vscode