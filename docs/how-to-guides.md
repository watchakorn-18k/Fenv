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

## Command for windows only

## Install packages

```
fenv install <package_name>
```

Install the package and add it to requirements.txt If the package name is omitted, the message `Maybe you forgot to put the name of the package to install? for example fenv install <package_name>` is displayed.

## Install packages

```
fenv uninstall <package_name>
```

Install the package and add it to requirements.txt
