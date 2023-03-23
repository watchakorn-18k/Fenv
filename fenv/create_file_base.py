""" Module creates a file called main.py and writes a function called main() inside of it"""
import os
from fenv.customizes.colors import Colors
from fenv.assets.commands import Commands
from fenv.env_all import EnvAll

Colors = Colors()
Commands = Commands()
notice = Colors.notice()
env_name = EnvAll()


class CreateFileBase:
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

    def create_file_main_py():
        """
        Create a file main.py and write a function called main() inside of it
        """
        file_path = "main.py"
        with open(file_path, "w") as f:
            f.write(Commands.get_main_py())
        os.chmod(file_path, 0o777)
        print(notice + f'Successfully created the file "{file_path}"')

    def generate_tree(startpath):
        output = ""
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, "").count(os.sep)
            if level == 0:
                indent = "    " * (level + 1) + "│   "
                subindent = "    " * (level + 2)
                for d in dirs:
                    dir_path = os.path.join(root, d)
                    output += f"{subindent}{'└──'}{d}/\n"
                    if d == ".vscode":
                        output += f"{subindent}{subindent}{'└──'}settings.json\n"
                    if d == env_name.get_env_name():
                        for i in ["Lib/", "Scripts", ".gitignore", "pyvenv.cfg"]:
                            output += f"{subindent}{subindent}{'└──'} {i}\n"

                for f in files:
                    file_path = os.path.join(root, f)
                    output += f"{subindent}{'└──'}{f}\n"
        print(os.getcwd())
        return output


def create_file_base(name, state):
    """
    Args:
        name (str): The name of the project
        state (str): The state of the project
    Example:
        ```py
        create_file_base("project_name")
        ```
    Return:
        None
    """

    def create_file_readme_md():
        """
        It creates a file called readme.md and writes the markdown text to it
        """
        markdown_path = "readme.md"
        markdown = """
# {}
A brief and descriptive title for your project.

## Description

A detailed description of the project, including its purpose, features, and any other relevant information.

## Getting Started

```
git clone https://github.com/<User Name Github>/{}.git

cd {}

```

## Installation

```
# create virtualenv auto name
fenv onlyenv

# install package in requirements.txt
fenv install

```

## Usage

Instructions on how to use the project, including any usage examples and screenshots.

## Tree
<!--- Start Tree --->
```bash
.
└── {}/
{}
```
<!--- End Tree --->

## Contributing

If you would like to contribute to the project, include a section on how to do so, including any guidelines and best practices.

## License

Include information about the license used for the project, such as the name of the license (e.g. MIT, Apache 2.0, etc.) and a link to the license text.

"""
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(markdown.format(name, name, name, name, generate_tree(".")))
        os.chmod(markdown_path, 0o777)
        print(notice + f'Successfully created the file "{markdown_path}"')

    def create_file_freeze():
        """
        It creates a file called "requirements.txt" and writes the string "black" to it
        """

        module_base = """black"""
        with open("requirements.txt", "w") as f:
            f.write(module_base)
        os.chmod("requirements.txt", 0o777)
        print(notice + f'Successfully created the file "requirements.txt"')

    def create_file_gitignore():
        """
        It creates a file called .gitignore and writes the string "*.pyc" to it
        """
        with open(".gitignore", "w") as f:
            f.write(f"*.pyc\n/{env_directory()}")
        os.chmod(".gitignore", 0o777)
        print(notice + f'Successfully created the file ".gitignore"')

    def update_file_readme_md():
        """
        It update a file called readme.md and writes the markdown text to it
        """
        markdown_path = "readme.md"
        with open(markdown_path, "r", encoding="utf-8") as f:
            data = f.readlines()

        for i, v in enumerate(data):
            if "<!--- Start Tree --->" in v:
                first = i

            if "<!--- End Tree --->" in v:
                last = i

        data = data[: first + 1] + data[last:]

        for i, v in enumerate(data):
            if "<!--- Start Tree --->" in v:
                data[
                    i
                ] = """
<!--- Start Tree --->
```bash
.
└── {}/
{}
```
""".format(
                    name, generate_tree(".")
                )
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.writelines(data)
        os.chmod(markdown_path, 0o777)

    """
    create_file_base main call function
    """
    if state == "create":
        create_file_main_py()
        create_file_freeze()
        create_file_gitignore()
        create_file_readme_md()
        update_file_readme_md()
    elif state == "update":
        update_file_readme_md()

    """
    end of create_file_base function 
    """
