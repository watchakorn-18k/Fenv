from argparse import ArgumentParser
import os
import platform
import re
import random


class bcolors:
    """It's a class that contains a bunch of variables that are strings of ANSI escape codes."""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"

    def __init__(self):
        self.HEADER = ""
        self.OKBLUE = ""
        self.OKGREEN = ""
        self.WARNING = ""
        self.FAIL = ""
        self.ENDC = ""


# Defining a variable called notice.
notice = (
    bcolors.OKBLUE
    + "["
    + bcolors.ENDC
    + bcolors.OKGREEN
    + "notice"
    + bcolors.OKBLUE
    + "]"
    + bcolors.ENDC
    + " "
)


def create_dir_file(path, text):
    """It creates a directory if it doesn't exist, and then creates a file in that directory with the given
    text

    Args:
        path (str): The path to the file you want to create
        text (str): The text to be written to the file

    Example:
        ```py
        create_dir_file(".vscode/settings.json", text_vscode.format(name_env=env_path))
        ```
    Return:
        None
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
    create_dir_file(".vscode/settings.json", text_vscode.format(name_env=env_path))
    print(notice + f"Successfully created the .vscode/settings.json")


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


""


def run_install_module_base(env):
    """
    It installs the base Python modules

    :param env: The environment object
    """

    if platform.system() == "Windows":
        os.system(f".\env_{env}\Scripts\python.exe -m pip install -r requirements.txt")
        print(notice + f'Successfully installed module in "requirements.txt"')
        os.system(f".\env_{env}\Scripts\python.exe -m pip freeze > requirements.txt")
        print(notice + f'Successfully updated the file "requirements.txt"')
        os.system(f".\env_{env}\Scripts\python.exe -m pip install --upgrade pip")


def create_project_all(args, name):
    """
    It creates a folder, creates a virtual environment, creates a settings file for VSCode, and creates
    a base file for the project
    """

    if create_folder(name) != 1:
        print(notice + "Creating...")
        create_virtualenv(name)
        create_setting_vscode(name)
        create_file_base(name)
        run_install_module_base(name)


def name_env():
    def cut_string(string, start, end) -> str:
        """
        It takes a string, finds the first occurrence of the start string, then finds the first
        occurrence of the end string after the start string, and returns the string between the start
        and end strings

        :param string: The string to cut from
        :param start: The string to start the search from
        :param end: The end of the string to cut
        :return: the string between the start and end strings.
        """
        start_index = string.find(start)
        if start_index == -1:
            return None

        end_index = string.find(end, start_index + len(start))
        if end_index == -1:
            return None

        return string[start_index + len(start) : end_index]

    def show_files_in_all_dirs(directory) -> str:
        """
        It takes a directory as an argument, iterates through the subdirectories in the main directory,
        and returns the name of the subdirectory that ends with "Lib"

        :param directory: The directory to search through
        :return: the result of the cut_string function.
        """
        for subdir, dirs, files in os.walk(directory):
            result = cut_string(subdir, ".\\", "\\Lib")
            if subdir[-3:] == "Lib":
                break
        return result

    return show_files_in_all_dirs(".")


def cmd_install_package(args):
    """
    It installs a package using pip

    :param args: The arguments passed to the command
    """
    try:
        if platform.system() == "Windows":
            os.system(
                f".\{name_env()}\Scripts\python.exe -m pip install {args.install}"
            )
            print(notice + f"Successfully installed module {args.install}")
    except TimeoutError:
        print(TimeoutError)


def add_module_to_txt(args):
    """
    It takes the argument from the command line and adds it to the requirements.txt file

    :param args: The arguments passed to the script
    """
    os.system(f"pip freeze > requirements.txt")
    print(notice + f'Successfully module {args.install} added to "requirements.txt"')


def find_dir_env() -> str:
    """
    It prints the contents of the current directory
    """
    for i in os.listdir("."):
        print(i)
    # .\{name_env()}\Scripts\python.exe -m pip uninstall {args.uninstall}


def install_package(args):
    """
    It takes a list of packages, and installs them using the `pip` command

    :param args: The arguments passed to the command
    """
    print(notice + "Installing...")
    cmd_install_package(args)
    add_module_to_txt(args)


def cmd_uninstall_package(args):
    """
    It uninstalls a package from the virtual environment

    :param args: The arguments passed to the command
    """
    try:
        if platform.system() == "Windows":
            os.system(
                f".\{name_env()}\Scripts\python.exe -m pip uninstall {args.uninstall}"
            )
            print(notice + f"Successfully uninstalled module {args.uninstall}")
    except TimeoutError:
        print(TimeoutError)


def remove_module_exit_txt(args):
    """
    It removes the module from the requirements.txt file

    :param args: This is the argument that is passed to the function
    """
    try:
        os.system(f"pip freeze > requirements.txt")
        print(
            notice
            + f'Successfully removed module {args.uninstall} exit from "requirements.txt"'
        )
    except Exception as e:
        print(f"Error: {e}")


def uninstall_package(args):
    """
    It takes a list of packages, and installs them using the `pip` command

    :param args: The arguments passed to the command
    """
    cmd_uninstall_package(args)
    remove_module_exit_txt(args)


def setup_parse():
    """
    It takes a list of strings, and returns a dictionary of the form {'name': 'value'}
    :return: The return value is a Namespace object.
    """

    parser = ArgumentParser(add_help=False)
    title = parser.add_argument_group(title="Usage")
    title.description = "fenv <command>"

    subparsers = parser.add_subparsers(title="Commands", dest="command", metavar="")

    new_comd = subparsers.add_parser("new", help="Create a new project")
    new_comd.add_argument(
        "new", type=str, help="The name of the project", nargs="?", default=None
    )

    install_cmd = subparsers.add_parser("install", help="Install packages")
    install_cmd.add_argument(
        "install",
        type=str,
        help="Install packages of the project packages",
        nargs="?",
        default=None,
    )

    uninstall_cmd = subparsers.add_parser("uninstall", help="Uninstall packages")
    uninstall_cmd.add_argument(
        "uninstall",
        type=str,
        help="Uninstall packages of the project packages",
        nargs="?",
        default=None,
    )

    update_cmd = subparsers.add_parser(
        "update", help="Update packages to file requirements.txt"
    )

    onlyenv_cmd = subparsers.add_parser(
        "onlyenv", help="Create only virtualenv and no create base file"
    )

    # clean_cmd = subparsers.add_parser(
    #     "clean", help="Clean delete all packages in requirements.txt out"
    # )

    general_group = parser.add_argument_group(title="General Options")
    general_group.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit"
    )

    args = parser.parse_args()

    return args


def run_cmd_new(args):
    """
    It creates a new project folder, and then creates a virtual environment inside that folder

    :param args: Namespace(new='test', project_folder='test')
    """
    try:
        create_project_all(args, args.new)
    except TypeError as err:
        print(
            "Maybe you forgot to enter the name of the folder? for example"
            + " `"
            + bcolors.OKGREEN
            + "fenv new"
            + bcolors.OKBLUE
            + " <project_folder>"
            + bcolors.ENDC,
            "`",
        )


def run_cmd_install(args):
    """
    It's a function that installs a package

    :param args: The arguments passed to the command
    """
    try:
        print("Installing...")
        install_package(args)
    except AttributeError as err:
        print(
            bcolors.OKGREEN
            + "An error was encountered, it could not be installed."
            + bcolors.ENDC
        )


def run_cmd_uninstall(args):
    """
    A function that is called when the user runs the command "uninstall"

    :param args: The arguments passed to the command
    """
    try:
        print(notice + "Uninstalling...")
        # uninstall_package(args)
    except AttributeError as err:
        print(err, "An error was encountered, it could not be uninstalled.")


def run_cmd_onlyenv():
    """
    It creates a virtual environment with a random name, and then creates a settings.json file for
    vscode
    """

    def create_name_env_auto() -> str:
        """
        > It creates a random name for the environment
        :return: A string
        """
        name_ = random.choice(["samai", "danai"])
        middle_ = random.choice("!@#$&$")
        no_ = random.randint(0, 100)
        return f"{name_}{middle_}{no_}"

    def create_name_env() -> str:
        """
        If the user enters a name for the virtualenv, the function will check if the name is in English
        only, if it is, it will return the name, if not, it will return a name automatically
        :return: The name of the virtual environment.
        """
        _name = input(
            "Enter a name for the virtualenv (english only) , leave it blank to create it automatically: "
        ).replace(" ", "_")

        def is_english_only(s):
            return bool(re.match("^[A-Za-z0-9_!@#$%^&*()\-+=]+$", s))

        if is_english_only(_name):
            _name = _name[:10]
            _name = "{}".format(_name)
            return _name
        else:
            _name = create_name_env_auto()
            return _name

    def create_virtualenv(virtual_env_name):
        """
        It creates a virtual environment with the name you pass to it

        :param virtual_env_name: The name of the virtual environment you want to create
        """
        if not os.path.exists(virtual_env_name):
            try:
                os.system(f"virtualenv env_{virtual_env_name}")
            except EnvironmentError as error:
                print(error)
        print(notice + f'Successfully created the virtualenv "{virtual_env_name}"')

    _name_env = create_name_env()
    print(f"your env name is `{bcolors.OKGREEN}{_name_env}{bcolors.ENDC}`")
    create_virtualenv(_name_env)
    create_setting_vscode(_name_env)


def run_cmd_clean():
    find_dir_env()


def check_command(args):
    """
    It checks the command that the user has entered and then runs the appropriate function

    :param args: The arguments passed to the script
    """
    if args.__dict__["command"] == "new":
        run_cmd_new(args)
    elif args.__dict__["command"] == "install":
        run_cmd_install(args) if args.install != None else print(
            "Maybe you forgot to put the name of the package to install? for example"
            + " `"
            + bcolors.OKGREEN
            + "fenv install"
            + bcolors.OKBLUE
            + " <package_name>"
            + bcolors.ENDC
            + "`"
        )
    elif args.__dict__["command"] == "uninstall":
        run_cmd_uninstall(args) if args.uninstall != None else print(
            "Maybe you forgot to put the name of the package to uninstall? for example"
            + " `"
            + bcolors.OKGREEN
            + "fenv uninstall"
            + bcolors.OKBLUE
            + " <package_name>"
            + bcolors.ENDC
            + "`"
        )
    elif args.__dict__["command"] == "update":
        os.system("pip freeze > requirements.txt")
        print(notice + "Updated module all to requirements.txt")
    elif args.__dict__["command"] == "onlyenv":
        run_cmd_onlyenv()

    elif args.__dict__["command"] == "clean":
        run_cmd_clean()


def main():
    """
    It takes the arguments from the command line and passes them to the create_project_all function
    """
    args = setup_parse()
    version: str = "v0.0.11"
    print(f"⏩ fenv {version}") if args.__dict__["command"] == None else None
    check_command(args)


# It's a way to make sure that the code in the `main` function is only run when the script is run.
# if __name__ == "__main__":
#     main()
