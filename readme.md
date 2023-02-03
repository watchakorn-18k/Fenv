# Fenv

<p align="center"><img src="https://cdn.discordapp.com/attachments/582486229594013696/1070509737529069689/New_Project_3.png" width=400></p>

Fenv is a simple and efficient tool to help you manage your virtual environments and create basic Python files with a single command. With Fenv, you can quickly generate a new project folder, establish a virtual environment within that folder, and simultaneously create the essential basic Python files all in one go. This tool is ideal for developers who frequently work on multiple Python projects and want a simple, streamlined solution for managing virtual environments.

## Features

- Generate a new project folder with a single command
- Quickly establish a virtual environment within the project folder
- Simultaneously create essential basic Python files
- Ideal for developers who work on multiple Python projects
- Add black for format python

<p align="center"><img src=https://media.discordapp.net/attachments/585068497495654413/1071136244437893201/gamedfdsf.gif" width=400></p>
<p align="center"><img src=https://media.discordapp.net/attachments/585068497495654413/1071136828498915358/gamedfdsf.gif" width=400></p>

# Installation

To install Fenv, simply run the following command:

```
pip install fenv
```

# Usage

Fenv makes it easy to get started with a new Python project by providing an all-in-one solution. Here's how to use it:

1. Create a new project folder:

```
fenv -new project_folder
```

2. Activate the virtual environment:

for windows

```
cd project_folder
source env/bin/activate
```

for linux

```
cd project_folder
source env/bin/activate
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
