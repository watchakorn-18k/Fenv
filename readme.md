<h1 align="center">Fenv</h1>

<p align="center"><img src="https://img.shields.io/github/languages/top/watchakorn-18k/Fenv?color=green&logo=python&logoColor=white">
<img src="https://img.shields.io/github/repo-size/watchakorn-18k/Fenv">
<img src="https://img.shields.io/pypi/dm/Fenv?logo=pypi&logoColor=white">
<img src="https://img.shields.io/pypi/v/Fenv?color=sd&label=Fenv&logoColor=white">
<img src="https://img.shields.io/github/v/release/watchakorn-18k/Fenv">
<img src="https://img.shields.io/pypi/pyversions/Fenv?logo=python&logoColor=white">
<img src="https://img.shields.io/website?url=https%3A%2F%2Fgithub.com%2Fwatchakorn-18k%2FFenv">
<img src="https://img.shields.io/github/last-commit/watchakorn-18k/Fenv?logo=git&style=social">
<img src="https://img.shields.io/github/stars/watchakorn-18k/Fenv?style=social">
</p>
<p align="center"><img src="https://cdn.discordapp.com/attachments/582486229594013696/1070509737529069689/New_Project_3.png" width=400></p>

Fenv is a simple and efficient tool to help you manage your virtual environments and create basic Python files with a single command. With Fenv, you can quickly generate a new project folder, establish a virtual environment within that folder, and simultaneously create the essential basic Python files all in one go. This tool is ideal for developers who frequently work on multiple Python projects and want a simple, streamlined solution for managing virtual environments.

## Features

- Generate a new project folder with a single command
- Quickly establish a virtual environment within the project folder
- Simultaneously create essential basic Python files
- Ideal for developers who work on multiple Python projects
- Add black for format python
- Packages can be installed and uninstalled and added to files. requirements.txt at the same time

## Docs

[Docs](https://watchakorn-18k.github.io/Fenv/)

## Volta planing

[Volta/Fenv](https://volta.net/watchakorn-18k/Fenv)

## Install

### Linux and macOS

```
pip install fenv
```

or

```
pip install --upgrade fenv
```

### Windows

If you are using Windows, you can install Fenv using pipx, which is a tool that allows you to install and run Python applications in isolated environments. This is a great way to install Fenv, as it will not interfere with any other Python applications you may have installed on your system.

**Note:** pipx only works with Python 3.6+.

First, install pipx using the following command:

```sh
py -m pip install --user pipx
```

```
py -m pipx ensurepath
```

Then, install Fenv using pipx:

```sh
pipx install fenv
```

**Note:** ensurepath ensures that the application directory is on your $PATH. You may need to restart your terminal for this update to take effect.

You may need to restart your terminal for this update to take effect.

## PyPi

```
https://pypi.org/project/Fenv/
```

## Start

```sh
fenv new <project_folder>
```

## Command

```cmd
$ fenv -h

usage: fenv [-h] [-v]  ...

Usage:
  fenv <command>

Commands:

    new          Create a new project
    install      Install the package and install the package via requirements.txt
    uninstall    Uninstall packages
    update       Package to file requirements.txt update furthermore, update the readme.md file's tree path.
    onlyenv      Create only virtualenv and no create base file
    clean        Clean delete all packages in requirements.txt out
    activate     Command hint to activate virtual environment with folder
    deactivate   Command hint to deactivate virtual environment with folder


General Options:
  -h, --help     Show this help message and exit
  -v, --version  check version fenv
```

## Install via setup.py

```
pip install --editable .
```

## Build

```
python setup.py sdist bdist_wheel
```

## Conclusion

Fenv is a powerful tool for managing virtual environments and creating basic Python files. With its simple and efficient design, it's the perfect solution for developers who want to streamline their workflow and focus on coding. Get started today and see the difference Fenv can make in your Python development process!

## Changelog

### 0.0.12.0
- [x] Add installation instructions for Windows users using pipx @yassine20011 [pull/5/files](https://github.com/watchakorn-18k/Fenv/pull/5/files)

### 0.0.11.9

- [x] Add command more `fenv deactivate` Command hint to deactivate virtual environment with folder
- [x] Add command more `fenv activate` Command hint to activate virtual environment with folder
      ![](https://i.imgur.com/H7MURw3.gif)

### 0.0.11.8

- Fix error ModuleNotFoundError: No module named 'dotenv' and not show version fenv

### 0.0.11.7

- [x] `fenv uninstall <package>` can remove packages and package dependencies all in one Tested [Windows]
  - before ![](https://i.imgur.com/2zRW1xY.gif)
  - after ![](https://i.imgur.com/oZ7LMN9.gif)
- [x] Add command `fenv clean` to clean packages left lib basic files pass test [Windows] and [Linux] ![](https://i.imgur.com/QPkGn0F.gif)
- [x] Added fev.cfg file
- [x] Support command all in Linux

### 0.0.11.6

- [x] Fix bug create readme.md change `env_directory()` to `name`

### 0.0.11.5

- [x] Added Tree path in md after generating projects , can you try command `fenv update` ![](https://i.imgur.com/vDz2Gs0.gif)
- [x] Added create file .gitignore
- [x] Edit readme.md small changes
- [x] Fix if an `env` folder does not exist, the modified `fenv install <packages>` command will prompt you to confirm whether you would like to create a new `env`. If you choose not to create a new `env`, the installation will proceed using `python main` ![](https://i.imgur.com/M0shh8x.gif)
- [x] Added command `fenv install` alone will install file requirements.txt in directory current ![](https://i.imgur.com/cgApbCa.gif)
- [x] Added after use `fenv onlyenv` created settings then activate env one time ![](https://i.imgur.com/mwEUSrg.gif)

### 0.0.11.4

- [x] Fix bugs small

### 0.0.11.3

- [x] Fix bugs settings in .vscode
- [x] Fix bugs line 609 and 624

### 0.0.11.2

- [x] Fix bugs small

### 0.0.11.1

- [x] Change new pattern command `-onlyenv` to `onlyenv`

### 0.0.10

- [x] Add option `-onlyenv` for create only virtualenv without base file all
- [x] Add command install for install package and add module to file requirements.txt

### 0.0.9

- [x] Release 0.0.9
