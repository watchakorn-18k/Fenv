# Fenv

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
https://watchakorn-18k.github.io/Fenv/

## Installer
```
pip install fenv
```
or
```
pip install --upgrade fenv
```

## Start

```sh
fenv new <project_folder>
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

## Build

```
python setup.py sdist bdist_wheel
```

## Testing

```
pip install --editable .
```

## Conclusion

Fenv is a powerful tool for managing virtual environments and creating basic Python files. With its simple and efficient design, it's the perfect solution for developers who want to streamline their workflow and focus on coding. Get started today and see the difference Fenv can make in your Python development process!

## Changelog

### 0.0.11.5
- [ ] added after use `fenv onlyenv` created settings then activate env one time 
### 0.0.11.4
- [x] fix bugs small
### 0.0.11.3
- [x] fix bugs settings in .vscode
- [x] fix bugs line 609 and 624
### 0.0.11.2
- [x] fix bugs small
### 0.0.11.1
- [x] change new pattern command `-onlyenv` to `onlyenv`
### 0.0.10
- [x] add option `-onlyenv` for create only virtualenv without base file all
- [X] add command install for install package and add module to file requirements.txt

### 0.0.9

- [x] Release 0.0.9
