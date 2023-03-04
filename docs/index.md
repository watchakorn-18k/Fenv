

![versions](https://img.shields.io/pypi/pyversions/pybadges.svg) ![](https://img.shields.io/badge/-version%200.11-blue)

# Fenv

<p align="center"><img src="https://cdn.discordapp.com/attachments/582486229594013696/1070509737529069689/New_Project_3.png" width=400></p>

Fenv is a simple and efficient tool to help you manage your virtual environments and create basic Python files with a single command. With Fenv, you can quickly generate a new project folder, establish a virtual environment within that folder, and simultaneously create the essential basic Python files all in one go. This tool is ideal for developers who frequently work on multiple Python projects and want a simple, streamlined solution for managing virtual environments.

## Features

- Generate a new project folder with a single command
- Quickly establish a virtual environment within the project folder
- Simultaneously create essential basic Python files
- Ideal for developers who work on multiple Python projects
- Add `black` for format python
- Packages can be installed and uninstalled and added to files. `requirements.txt` at the same time

## Installer
```
pip install fenv
```
or
```
pip install --upgrade fenv
```

## Command

```cmd
$ fenv -h

Usage:
  fenv [options] <command>

Commands:

    new       Create a new project
    install   Install packages
    uninstall Uninstall packages
    update    Update packages to file requirements.txt
    onlyenv   Create only virtualenv and no create base file

General Options:
  -h, --help  Show this help message and exit

```

## Layout

    |_ .vscode/
    |    |_ settings.json
    |
    |_ env_name/
    |    |_ Lib
    |    |_ Scripts
    |    |_ .gitignore
    |    |_ pyvenv
    |
    |_ main.py
    |_ readme.md
    |_ requirements.txt
