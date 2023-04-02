![versions](https://img.shields.io/pypi/pyversions/pybadges.svg) ![](https://img.shields.io/badge/-version%200.11.9-blue)

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

## PyPi

```
https://pypi.org/project/Fenv/
```

## Command

```cmd
usage: fenv [-h] [-v]  ...

Usage:
  fenv <command>

Commands:

    new          Create a new project
    install      Install the package and install the
                 package via requirements.txt
    uninstall    Uninstall packages
    update       Package to file requirements.txt update
                 furthermore, update the readme.md file's
                 tree path.
    onlyenv      Create only virtualenv and no create
                 base file

General Options:
  -h, --help     Show this help message and exit
  -v, --version  check version fenv

```

## Layout

```
└── test/
        └──.vscode/
                └──settings.json
        └──env_test/
                └── Lib/
                └── Scripts
                └── .gitignore
                └── pyvenv.cfg
        └──.gitignore
        └──main.py
        └──readme.md
        └──requirements.txt
```
