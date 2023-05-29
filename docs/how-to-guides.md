# How to guides

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

# Command for windows and linux only

## Install packages

```
fenv install
```

One command can be used to install packages from requirements.txt, and if Fenv's virtual environment does not exist, it will prompt the user to create it. However, an error message will be displayed if the requirements.txt file cannot be located.

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
fenv env
```

Create a virtualenv with a custom name or an optional 2 autoname, then create a file. settings.json for vscode does not generate additional base files

## Cleanup packages all

```
fenv clean
```

Clean, remove all packages like new.

## Activate the virtual environment

```
fenv activate
```

Activate the virtual environment if the terminal is not supported will show a hint.

~~`fenv deactivate`~~ **_currently not in use_**

```
fenv clone [url_repo]
```

Clone data from repositories and create virtualenv.
