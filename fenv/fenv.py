from argparse import ArgumentParser, Namespace
import os
import platform


# It's a class that contains a bunch of variables that are strings of ANSI escape codes.
class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        """
        It sets the color variables to empty strings, which means that when you call them, they will
        return an empty string
        """
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


notice = bcolors.OKBLUE + \
    '['+bcolors.ENDC+bcolors.OKGREEN+'notice' + \
    bcolors.OKBLUE + ']' + bcolors.ENDC + " "


def create_dir_file(path, text):
    """
    It creates a directory if it doesn't exist, and then creates a file in that directory with the given
    text

    :param path: The path to the file you want to create
    :param text: The text to be written to the file
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def create_virtualenv(virtual_env_name):
    """
    It creates a virtual environment in the current directory

    :param virtual_env_name: The name of the virtual environment you want to create
    """
    os.chdir(virtual_env_name)
    if not os.path.exists(virtual_env_name):
        try:
            os.system(f"virtualenv env_{virtual_env_name}")
        except EnvironmentError as error:
            print(error)
    print(notice + f'Successfully created the virtualenv "{virtual_env_name}"')


def create_folder(folder_name):
    """
    It creates a folder with the name of the argument passed to it

    :param folder_name: The name of the folder you want to create
    :return: 1
    """
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(notice + f"{folder_name} already exists.")
        return 1
    else:
        print(notice + f'Successfully created the directory "{folder_name}"')


def create_setting_vscode(env_path):
    """
    It creates a file called `settings.json` in a directory called `.vscode` in the current directory. 

    The file contains a JSON object with two keys: `python.formatting.provider` and `python.pythonPath`.


    The value of the first key is `black` and the value of the second key is the path to the virtual
    environment. 

    The third key is `editor.formatOnSave` and its value is `true`. 

    The function prints a message to the console when it's done. 

    The function is called in the `create_env` function. 

    The `create_env` function is called in the `main` function. 

    The `main` function is called when the script is run. 

    The `create_env` function is called with the name of the virtual environment as an argument. 

    The

    :param env_path: The path to the virtual environment
    """
    text_vscode = """{{"python.formatting.provider": "black","python.pythonPath": "{name_env}","editor.formatOnSave": true,}}"""
    create_dir_file(
        '.vscode/settings.json', text_vscode.format(name_env=env_path))
    print(notice + f'Successfully created the .vscode/settings.json')


def create_file_base(name):
    """
    It creates a file called main.py and writes a function called main() inside of it

    :param name: The name of the project
    """
    def create_file_main_py():
        """
        It creates a file called main.py and writes a function called main() inside of it
        """

        file_path = "main.py"
        command = """
def main():
    pass


if __name__ == "__main__":
    main()
    """
        with open(file_path, "w") as f:
            f.write(command)
        os.chmod(file_path, 0o777)
        print(notice + f'Successfully created the file "{file_path}"')

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
pip install -r requirements.txt
```

## Usage

Instructions on how to use the project, including any usage examples and screenshots.

## Contributing

If you would like to contribute to the project, include a section on how to do so, including any guidelines and best practices.

## License

Include information about the license used for the project, such as the name of the license (e.g. MIT, Apache 2.0, etc.) and a link to the license text.

"""
        with open(markdown_path, "w") as f:
            f.write(markdown.format(name))
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

    create_file_main_py()
    create_file_readme_md()
    create_file_freeze()


''


def run_install_module_base(env):
    """
    It installs the base Python modules

    :param env: The environment object
    """

    if platform.system() == "Windows":
        os.system(
            f".\env_{env}\Scripts\python.exe -m pip install -r requirements.txt")
        print(notice + f'Successfully installed module in "requirements.txt"')
        os.system(
            f".\env_{env}\Scripts\python.exe -m pip freeze > requirements.txt")
        print(notice + f'Successfully updated the file "requirements.txt"')
        os.system(
            f".\env_{env}\Scripts\python.exe -m pip install --upgrade pip")


def create_project_all(args, name):
    """
    It creates a folder, creates a virtual environment, creates a settings file for VSCode, and creates
    a base file for the project
    """
    if create_folder(name) != 1:
        create_virtualenv(name)
        create_setting_vscode(name)
        if not args.onlyenv:
            create_file_base(name)
            run_install_module_base(name)


def setup_parse():
    """
    It takes a list of strings, and returns a dictionary of the form {'name': 'value'}
    :return: The return value is a Namespace object.
    """

    parser = ArgumentParser(add_help=False)
    title = parser.add_argument_group(title='Usage')
    title.description = "fenv [options] <command>"

    subparsers = parser.add_subparsers(
        title='Commands', dest='command', metavar="")

    new_parser = subparsers.add_parser('new', help='Create a new project')
    new_parser.add_argument('new', type=str,
                            help='The name of the project')

    new_parser1 = subparsers.add_parser('install', help='Install packages')
    new_parser1.add_argument('install', type=str,
                             help='The name of the project packages')

    general_group = parser.add_argument_group(title='General Options')
    general_group.add_argument(
        '-h', '--help', action='help', help='Show this help message and exit')
    general_group.add_argument('-onlyenv', action='store_true',
                               help='Create only virtualenv and no create base file')

    args = parser.parse_args()

    return args


def main():
    """
    It takes the arguments from the command line and passes them to the create_project_all function
    """
    args = setup_parse()
    print(args, "⏩ fenv v0.0.10") if args.__dict__['command'] == None else None
    try:
        if args.new:
            create_project_all(args, args.new)
    except AttributeError as err:
        print(notice +
              args.__dict__['command']+"ing package") if args.__dict__['command'] != None else None


# It's a way to make sure that the code in the `main` function is only run when the script is run.
# if __name__ == "__main__":
#     main()
