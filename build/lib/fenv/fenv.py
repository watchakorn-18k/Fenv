from argparse import ArgumentParser
import os
import platform
import re
import random
import fnmatch


class bcolors:
    """It's a class that contains a bunch of variables that are strings of ANSI escape codes.
    Example:
        ```
        Colors.HEADER
        Colors.OKBLUE
        Colors.OKGREEN
        Colors.WARNING
        Colors.FAIL
        Colors.ENDC
        ```
    Return:
        None
    """


class Colors:
    ESCAPE_SEQ = {
        "HEADER": "\033[95m",
        "OKBLUE": "\033[94m",
        "OKGREEN": "\033[92m",
        "WARNING": "\033[93m",
        "FAIL": "\033[91m",
        "ENDC": "\033[0m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
    }

    TEXT_COLORS = {
        "BLACK": "\033[30m",
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "MAGENTA": "\033[35m",
        "CYAN": "\033[36m",
        "WHITE": "\033[37m",
    }

    LIGHT_COLORS = {
        "LIGHTBLACK_EX": "\033[90m",
        "LIGHTRED_EX": "\033[91m",
        "LIGHTGREEN_EX": "\033[92m",
        "LIGHTYELLOW_EX": "\033[93m",
        "LIGHTBLUE_EX": "\033[94m",
        "LIGHTMAGENTA_EX": "\033[95m",
        "LIGHTCYAN_EX": "\033[96m",
        "LIGHTWHITE_EX": "\033[97m",
    }

    COLOR256 = {
        "PURPLE": "\033[38;5;129m",
        "ORANGE": "\033[38;5;202m",
        "BROWN": "\033[38;5;130m",
        "OLIVE": "\033[38;5;142m",
        "GOLD": "\033[38;5;214m",
        "SILVER": "\033[38;5;188m",
        "MAROON": "\033[38;5;52m",
        "NAVY": "\033[38;5;21m",
        "TEAL": "\033[38;5;29m",
        "LIME": "\033[38;5;118m",
        "AQUA": "\033[38;5;45m",
        "FUSCHIA": "\033[38;5;161m",
        "PURPLE2": "\033[38;5;98m",
        "PLUM": "\033[38;5;88m",
        "INDIGO": "\033[38;5;54m",
        "TURQUOISE": "\033[38;5;80m",
        "STEEL_BLUE": "\033[38;5;67m",
        "ROSE": "\033[38;5;210m",
        "HOT_PINK": "\033[38;5;200m",
        "SALMON": "\033[38;5;173m",
        "CORAL": "\033[38;5;203m",
        "BEIGE": "\033[38;5;230m",
        "KHAKI": "\033[38;5;143m",
        "FOREST_GREEN": "\033[38;5;34m",
        "OLIVE_GREEN": "\033[38;5;58m",
        "LAVENDER": "\033[38;5;183m",
        "ORCHID": "\033[38;5;170m",
        "LILAC": "\033[38;5;134m",
        "SKY_BLUE": "\033[38;5;117m",
        "BABY_BLUE": "\033[38;5;152m",
        "POWDER_BLUE": "\033[38;5;165m",
        "SEA_GREEN": "\033[38;5;27m",
        "PALE_GREEN": "\033[38;5;120m",
        "SPRING_GREEN": "\033[38;5;48m",
        "MINT_GREEN": "\033[38;5;121m",
        "GRAY_BLUE": "\033[38;5;103m",
        "BLUE_GRAY": "\033[38;5;104m",
    }

    def __getattr__(self, name):
        if name in self.ESCAPE_SEQ:
            return self.ESCAPE_SEQ[name]
        elif name in self.TEXT_COLORS:
            return self.TEXT_COLORS[name]
        elif name in self.LIGHT_COLORS:
            return self.LIGHT_COLORS[name]
        elif name in self.COLOR256:
            return self.COLOR256[name]
        else:
            raise AttributeError


Colors = Colors()
# Defining a variable called notice.
notice = (
    Colors.OKBLUE
    + "["
    + Colors.ENDC
    + Colors.OKGREEN
    + "notice"
    + Colors.OKBLUE
    + "]"
    + Colors.ENDC
    + " "
)


def env_directory():
    """It's a function that checks if the environment directory exists.
    Return:
        [] : empyt list
    """
    folder_name = "env*"
    return (
        fnmatch.filter(os.listdir("."), folder_name)
        if fnmatch.filter(os.listdir("."), folder_name) == []
        else str(fnmatch.filter(os.listdir("."), folder_name)[0])
    )


def root_directory():
    """It's a function that checks if the root directory exists.

    Return:
        str : root directory
    """
    return os.path.basename(os.path.abspath("."))


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

    :param virtual_env_name (str): The name of the virtual environment you want to create
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

     Args:
        folder_name (str): The name of the folder you want to create

    Example:
        ```py
        create_folder("project_name")
        ```
    Return:
        1 : if has folder already
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
    It creates a file called settings.json in a directory called .vscode.

    The file contains a JSON object with two keys:

    - python.formatting.provider
    - python.pythonPath

    The value of the first key is the string "black".

    The value of the second key is the path to the virtual environment.

    The function also prints a message to the console.

    The message is a string that contains the value of the global variable notice.

    The message also contains the string "Successfully created the .vscode/settings.json".

    The function ends with the keyword def.

    The function is called create_setting_vscode.

    The function takes one argument.

    The argument is called env_path.

    The function begins with the keyword def.

    The function ends with the

    Args:
      env_path (str): The path to the virtual environment
    Example:
        ```py
        create_setting_vscode("env_path")
        ```
    Return:
        None
    """

    text_vscode = """{{"python.formatting.provider": "black","python.pythonPath": "{name_env}","editor.formatOnSave": true,}}"""
    create_dir_file(".vscode/settings.json", text_vscode.format(name_env=env_path))
    print(notice + f"Successfully created the .vscode/settings.json")


def create_file_base(name, state):
    """
    It creates a file called main.py and writes a function called main() inside of it

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
                    if d == env_directory():
                        for i in ["Lib/", "Scripts", ".gitignore", "pyvenv.cfg"]:
                            output += f"{subindent}{subindent}{'└──'} {i}\n"

                for f in files:
                    file_path = os.path.join(root, f)
                    output += f"{subindent}{'└──'}{f}\n"
        print(os.getcwd())
        return output

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
            f.write(
                markdown.format(name, name, name, env_directory(), generate_tree("."))
            )
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
                    env_directory(), generate_tree(".")
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


def create_project_all(name):
    """
    It creates a folder, creates a virtual environment, creates a settings file for VSCode, and creates
    a base file for the project

    Args:
      name (str): The name of the folder you want to create

    Example:
        ```py
        create_project_all("project_name")
        ```
    Return:
        None
    """

    if create_folder(name) != 1:
        print(notice + "Creating...")
        create_virtualenv(name)
        create_setting_vscode(name)
        create_file_base(name, "create")
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

    Args:
        args (str): The arguments passed to the command
    Example:
        ```py
        cmd_install_package("package_name")
        ```
    Return:
        None
    """
    try:
        if platform.system() == "Windows":
            os.system(
                f".\{env_directory()}\Scripts\python.exe -m pip install {args.install}"
            )
            print(notice + f"Successfully installed module {args.install}")
    except TimeoutError:
        print(TimeoutError)


def add_module_to_txt(args):
    """
    It takes the argument from the command line and adds it to the requirements.txt file
    Args:
        args (str): The arguments passed to the script

    Example:
        ```py
        add_module_to_txt("package_name")
        ```
    Return:
        None

    """
    if env_directory():
        os.system(
            f".\{env_directory()}\Scripts\python.exe -m pip freeze > requirements.txt"
        )
        print(
            notice + f'Successfully module {args.install} added to "requirements.txt"'
        )


def find_dir_env() -> str:
    """
    It prints the contents of the current directory

    Return:
        None
    """
    for i in os.listdir("."):
        print(i)
    # .\{name_env()}\Scripts\python.exe -m pip uninstall {args.uninstall}


def install_package(args):
    """
    It takes a list of packages, and installs them using the `pip` command

    Args:
      args (str): The arguments passed to the command
    Example:
        ```py
        install_package("package_name")
        ```
    Return:
        None
    """
    print(notice + "Installing...")
    cmd_install_package(args)
    add_module_to_txt(args)


def cmd_uninstall_package(args):
    """
    It uninstalls a package from the virtual environment

    Args:
        args (str): The arguments passed to the command
    Example:
        ```py
        cmd_uninstall_package("package_name")
        ```
    Return:
        None
    """
    try:
        if platform.system() == "Windows":
            os.system(
                f".\{env_directory()}\Scripts\python.exe -m pip uninstall {args.uninstall}"
            )
            print(notice + f"Successfully uninstalled module {args.uninstall}")
    except TimeoutError:
        print(TimeoutError)


def remove_module_exit_txt(args):
    """
    It removes the module from the requirements.txt file

    Args:
      args (str): This is the argument that is passed to the function.
    Example:
        ```py
        remove_module_exit_txt("package_name")
        ```
    Return:
        None
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
    It will uninstall the package and remove the module exit text file

    Args:
      args (str): The arguments passed to the script.
    Example:
        ```py
        uninstall_package("package_name")
        ```
    Return:
        None
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

    install_cmd = subparsers.add_parser(
        "install",
        help="Install the package and install the package via requirements.txt",
        usage=f"{Colors.NAVY}fenv install {Colors.NAVY}<package_name>{Colors.ENDC} or {Colors.HOT_PINK}fenv install {Colors.ENDC}",
    )
    install_cmd.add_argument(
        "install",
        type=str,
        help="Install packages of the project packages",
        nargs="?",
        default=None,
    )

    uninstall_cmd = subparsers.add_parser(
        "uninstall",
        help="Uninstall packages",
        usage=f"{Colors.HOT_PINK}fenv uninstall <package_name>{Colors.ENDC}",
    )
    uninstall_cmd.add_argument(
        "uninstall",
        type=str,
        help="Uninstall packages of the project packages",
        nargs="?",
        default=None,
    )

    update_cmd = subparsers.add_parser(
        "update",
        help="Package to file requirements.txt update furthermore, update the readme.md file's tree path.",
        usage=f"{Colors.HOT_PINK}fenv update{Colors.ENDC}",
    )

    onlyenv_cmd = subparsers.add_parser(
        "onlyenv",
        help=f"Create only virtualenv and no create base file",
        usage=f"{Colors.HOT_PINK}fenv onlyenv{Colors.ENDC}",
    )

    # clean_cmd = subparsers.add_parser(
    #     "clean", help="Clean delete all packages in requirements.txt out"
    # )

    general_group = parser.add_argument_group(title="General Options")
    general_group.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit"
    )
    general_group.add_argument(
        "-v", "--version", action="store_true", help="check version fenv"
    )

    args = parser.parse_args()

    return args


def run_cmd_new(args):
    """
    It creates a new project folder and then creates a virtual environment inside that folder

    Args:
      args (str): The arguments passed to the command.
    Example:
        ```py
        run_cmd_new("project_name")
        ```
    Return:
        None
    """

    try:
        create_project_all(args.new)
    except TypeError as err:
        print(
            "Maybe you forgot to enter the name of the folder? for example"
            + " `"
            + Colors.MINTGREEN
            + "fenv new"
            + Colors.NAVY
            + " <project_folder>"
            + Colors.ENDC,
            "`",
        )


def run_cmd_install(args):
    """
    It tries to install a package, if it fails, it prints a message

    Args:
      args (str): The arguments passed to the command.
    Example:
        ```py
        run_cmd_install("package_name")
        ```
    Return:
        None
    """

    try:
        if env_directory():
            install_package(args)
        else:
            while True:
                response = input(
                    "We couldn't find the fenv virtual environment. Would you like to set up a new one? (y/n): "
                )
                if (
                    response.lower() == "y"
                    or response.lower() == "yes"
                    or response.lower() == ""
                ):
                    run_cmd_onlyenv()
                    folder_name = "env*"
                    folder_name_env = str(
                        fnmatch.filter(os.listdir("."), folder_name)[0]
                    )
                    install_package(args)
                    break
                elif response.lower() == "n":
                    install_package(args)
                    break
    except AttributeError as err:
        print(
            Colors.MINTGREEN
            + "An error was encountered, it could not be installed."
            + Colors.ENDC
        )


def install_package_all():
    """
    install all packages in requirements.txt file using pip install -r requirements.txt
    """

    folder_name = "env*"
    folder_name_env = (
        fnmatch.filter(os.listdir("."), folder_name)
        if fnmatch.filter(os.listdir("."), folder_name) == []
        else str(fnmatch.filter(os.listdir("."), folder_name)[0])
    )
    requirements_file = "requirements.txt"

    def install_package_follow_env(folder_name_env):
        if platform.system() == "Windows":
            os.system(
                f".\{folder_name_env}\Scripts\python.exe -m pip install -r requirements.txt"
            )

    def run_install_main(folder_name_env):
        if folder_name_env:
            print(
                f"Found directory  `{Colors.MINTGREEN}{folder_name_env}{Colors.ENDC}`"
            )
            print(
                f"Installing modules with  `{Colors.MINTGREEN}{folder_name_env}{Colors.ENDC}`"
            )
            install_package_follow_env(folder_name_env)
            print(notice + f'Successfully installed module from "requirements.txt"')
        else:
            while True:
                response = input(
                    "We couldn't find the fenv virtual environment. Would you like to set up a new one? (y/n): "
                )
                if (
                    response.lower() == "y"
                    or response.lower() == "yes"
                    or response.lower() == ""
                ):
                    run_cmd_onlyenv()
                    folder_name = "env*"
                    folder_name_env = str(
                        fnmatch.filter(os.listdir("."), folder_name)[0]
                    )
                    print(
                        f"Installing modules with  `{Colors.MINTGREEN}{folder_name_env}{Colors.ENDC}`"
                    )
                    install_package_follow_env(folder_name_env)
                    print(
                        notice
                        + f'Successfully installed module from "requirements.txt"'
                    )
                    break
                elif response.lower() == "n":
                    os.system(f"pip install -r requirements.txt")
                    break

    if requirements_file in os.listdir("."):
        run_install_main(folder_name_env)
    else:
        print(
            f"Maybe you forgot to put the name of the package to ininstall? for example `{Colors.MINTGREEN}fenv ininstall{Colors.OKBLUE} <package_name>{Colors.ENDC}` \nOr you can use `{Colors.MINTGREEN}fenv ininstall{Colors.ENDC}` alone. But there must be {Colors.FAIL}{requirements_file}{Colors.ENDC} in the current directory"
        )


def run_cmd_uninstall(args):
    """
    "A function that is called when the user runs the command "uninstall"."

    The first line of the function is a docstring. It's a string that describes what the function does.
    It's a good idea to include a docstring for every function you write

    Args:
      args (str): The arguments passed to the command
    Example:
        ```py
        run_cmd_uninstall("package_name")
        ```
    Return:
        None
    """
    try:
        print(notice + "Uninstalling...")
        uninstall_package(args)
    except AttributeError as err:
        print(err, "An error was encountered, it could not be uninstalled.")


def run_cmd_onlyenv():
    """
    It creates a virtual environment with a random name, and then creates a settings.json file for
    vscode
    Return:
        None
    """

    def create_name_env_auto() -> str:
        """
        > It creates a random name for the environment
        :return: A string
        """
        name_ = random.choice(["samai", "danai"])
        middle_ = random.choice("_#")
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
            return bool(re.match("^[A-Za-z0-9_#]+$", s))

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

        Args:
          virtual_env_name (str): The name of the virtual environment you want to create.

        Example:
            ```py
            create_virtualenv("virtual_env_name")
            ```
        Return:
            None
        """

        if not os.path.exists(virtual_env_name):
            try:
                os.system(f"virtualenv env_{virtual_env_name}")
            except EnvironmentError as error:
                print(error)
        print(notice + f'Successfully created the virtualenv "{virtual_env_name}"')

    _name_env = create_name_env()
    print(f"your env name is `{Colors.MINTGREEN}{_name_env}{Colors.ENDC}`")
    create_virtualenv(_name_env)
    dir_name_only = os.path.basename(os.getcwd())  # get name dir main
    create_setting_vscode(dir_name_only)


def run_cmd_clean():
    """
    It finds the directory of the environment that you're currently in, and then runs the command `conda
    clean --all` in that directory
    Return:
        None
    """
    find_dir_env()


def check_command(args):
    """
    It checks the command that the user has entered and then runs the appropriate function

    Args:
        args (str): The arguments passed to the script

    Example:
        ```py
        check_command("new" or "install" or "uninstall" or "update" or "onlyenv")
        ```
    Return:
        None
    """
    if args.__dict__["command"] == "new":
        run_cmd_new(args)
    elif args.__dict__["command"] == "install":
        run_cmd_install(args) if args.install != None else install_package_all()

    elif args.__dict__["command"] == "uninstall":
        run_cmd_uninstall(args) if args.uninstall != None else print(
            "Maybe you forgot to put the name of the package to uninstall? for example"
            + " `"
            + Colors.MINTGREEN
            + "fenv uninstall"
            + Colors.OKBLUE
            + " <package_name>"
            + Colors.ENDC
            + "`"
        )
    elif args.__dict__["command"] == "update":
        create_file_base(root_directory(), "update")
        print(notice + "Updated tree path to readme.md")
        os.system("pip freeze > requirements.txt")
        print(notice + "Updated module all to requirements.txt")
    elif args.__dict__["command"] == "onlyenv":
        run_cmd_onlyenv()

    # elif args.__dict__["command"] == "clean":
    #     run_cmd_clean()


def main():
    """
    It takes the arguments from the command line and passes them to the create_project_all function
    Return:
        None
    """
    args = setup_parse()
    version: str = "v0.0.11.5"
    print(
        f"⏩ {Colors.LIGHTMAGENTA_EX}Hello,Fenv {Colors.POWDER_BLUE}[{Colors.MINT_GREEN}{version}{Colors.POWDER_BLUE}]{Colors.ENDC}🫡\n".center(
            40, "-"
        )
    ) if args.__dict__["command"] == None else None
    check_command(args)

    # Colors.HEADER
    # Colors.OKBLUE
    # Colors.OKGREEN
    # Colors.WARNING
    # Colors.FAIL
    # Colors.ENDC


# It's a way to make sure that the code in the `main` function is only run when the script is run.
# if __name__ == "__main__":
#     main()
