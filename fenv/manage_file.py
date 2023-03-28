""" Module manage create file """
import os
import platform
import re
import random
import fnmatch
from fenv.customizes.colors import Colors
from fenv.assets.commands import Commands
from fenv.env_all import EnvAll


class CreateFileBaseAndUpdate:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.colors = Colors()
        self.notice = Colors().notice()
        self.commands = Commands()
        self.env_directory = EnvAll().get_env_name()
        self.root_directory = EnvAll().get_root_dir_name()

    def create_file_main_py(self):
        """
        Create a file main.py and write a function called main() inside of it
        """
        self.file_path = "main.py"
        with open(self.file_path, "w") as f:
            f.write(self.commands.get_main_py())
        os.chmod(self.file_path, 0o777)
        print(self.notice + f'Successfully created the file "{self.file_path}"')

    def generate_tree(self):
        self.output = ""
        for root, dirs, files in os.walk("."):
            level = root.replace(".", "").count(os.sep)
            if level == 0:
                indent = "    " * (level + 1) + "│   "
                subindent = "    " * (level + 2)

                for d in dirs:
                    dir_path = os.path.join(root, d)
                    self.output += f"{subindent}{'└──'}{d}/\n"
                    if d == ".vscode":
                        self.output += f"{subindent}{subindent}{'└──'}settings.json\n"
                    if d == self.env_directory:
                        for i in ["Lib/", "Scripts", ".gitignore", "pyvenv.cfg"]:
                            self.output += f"{subindent}{subindent}{'└──'} {i}\n"

                for f in files:
                    file_path = os.path.join(root, f)
                    self.output += f"{subindent}{'└──'}{f}\n"

        return self.output

    def create_file_readme_md(self):
        """
        It creates a file called readme.md and writes the markdown text to it
        """
        markdown_path = "readme.md"
        markdown = self.commands.get_readme_md()
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(
                markdown.format(
                    self.name, self.name, self.name, self.name, self.generate_tree()
                )
            )
        os.chmod(markdown_path, 0o777)
        print(self.notice + f'Successfully created the file "{markdown_path}"')

    def create_file_freeze(self):
        """
        It creates a file called "requirements.txt" and writes the string "black" to it
        """
        module_base = self.commands.get_requirements_txt()
        with open("requirements.txt", "w") as f:
            f.write(module_base)
        os.chmod("requirements.txt", 0o777)
        print(self.notice + f'Successfully created the file "requirements.txt"')

    def create_file_gitignore(self):
        """
        It creates a file called .gitignore and writes the string "*.pyc" to it
        """
        with open(".gitignore", "w") as f:
            f.write(f"*.pyc\n/{self.env_directory}")
        os.chmod(".gitignore", 0o777)
        print(self.notice + f'Successfully created the file ".gitignore"')

    def update_file_readme_md(self):
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
                data[i] = self.commands.get_update_tree_path().format(
                    self.name, self.generate_tree()
                )
        with open(markdown_path, "w", encoding="utf-8") as f:
            f.writelines(data)
        os.chmod(markdown_path, 0o777)

    def create_virtualenv(self):
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
        if os.path.exists(self.name):
            os.chdir(self.name)
            print(f"createing virtualenv env_{self.name}...")
            os.system(f"virtualenv env_{self.name}")
            EnvAll().create_lib_default_env()

        print(self.notice + f'Successfully created the virtualenv "{self.name}"')

    def create_setting_vscode(self):
        """
        It creates a file settings.json inside the virtual environment
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
        os.makedirs(os.path.dirname(".vscode/settings.json"), exist_ok=True)
        with open(".vscode/settings.json", "w", encoding="utf-8") as f:
            f.write(text_vscode.format(name_env=self.name))
        print(self.notice + f"Successfully created the .vscode/settings.json")

    def run_install_module_base(self):
        """
        It installs the base Python modules

        :param env: The environment object
        """

        if platform.system() == "Windows":
            os.system(
                f".\env_{self.name}\Scripts\python.exe -m pip install -r requirements.txt"
            )
            print(self.notice + f'Successfully installed module in "requirements.txt"')
            os.system(
                f".\env_{self.name}\Scripts\python.exe -m pip freeze > requirements.txt"
            )
            print(self.notice + f'Successfully updated the file "requirements.txt"')
            os.system(
                f".\env_{self.name}\Scripts\python.exe -m pip install --upgrade pip"
            )

        elif platform.system() == "Linux":
            os.system(
                f"bash -c 'source env_{self.name}/bin/activate  && pip install -r requirements.txt'"
            )
            print(self.notice + f'Successfully installed module in "requirements.txt"')
            os.system(
                f"bash -c 'source env_{self.name}/bin/activate  && pip freeze > requirements.txt'"
            )
            print(self.notice + f'Successfully updated the file "requirements.txt"')
            os.system(
                f"bash -c 'source env_{self.name}/bin/activate  && pip install --upgrade pip'"
            )

    def create_folder(self):
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
            os.mkdir(self.name)
        except FileExistsError:
            print(self.notice + f"{self.name} already exists.")
            return 1
        else:
            print(self.notice + f'Successfully created the directory "{self.name}"')

    def process_create_base_file_and_update(self):
        """
        If the state is create, create the files main.py, freeze.py, gitignore.py, and readme.md. If the
        state is update, update the file readme.md
        """
        if self.state == "create":
            self.create_file_main_py()
            self.create_file_freeze()
            self.create_file_gitignore()
            self.create_file_readme_md()
            self.update_file_readme_md()
        elif self.state == "update":
            self.update_file_readme_md()

    def procress_only_create_project(self):
        """
        It creates a virtual environment and a vscode settings file.
        """
        if self.create_folder() != 1:
            self.create_virtualenv()
            self.create_setting_vscode()
            self.process_create_base_file_and_update()
            self.run_install_module_base()


class OnlyVirtualEnv:
    """Module create only env"""

    def __init__(self):
        self.colors = Colors()
        self.notice = Colors().notice()
        self.commands = Commands()
        self.env_directory = EnvAll().get_env_name()
        self.root_directory = EnvAll().get_root_dir_name()

    def create_name_env_auto(self) -> str:
        """
        > It creates a random name for the environment
        :return: A string
        """
        self.name_ = random.choice(["samai", "danai"])
        self.middle_ = random.choice("_#")
        self.no_ = random.randint(0, 100)
        return f"{self.name_}{self.middle_}{self.no_}"

    def create_name_env(self) -> str:
        """
        If the user enters a name for the virtualenv, the function will check if the name is in English
        only, if it is, it will return the name, if not, it will return a name automatically
        :return: The name of the virtual environment.
        """
        self.name = input(
            "Enter a name for the virtualenv (english only) , leave it blank to create it automatically: "
        ).replace(" ", "_")

        if bool(re.match("^[A-Za-z0-9_#]+$", self.name)):
            return "{}".format(self.name[:10])
        else:
            return self.create_name_env_auto()

    def create_virtualenv_not_change_dir(self):
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
        if not os.path.exists(self._name_env):
            print(f"virtualenv env_{self._name_env}")
            os.system(f"virtualenv env_{self._name_env}")
            EnvAll().create_lib_default_env()

        print(self.notice + f'Successfully created the virtualenv "{self._name_env}"')

    def run_process(self):
        """
        It creates a virtual environment and a vscode settings file.
        """
        self._name_env = self.create_name_env()
        print(
            f"your env name is `{self.colors.LIGHTGREEN_EX}{self._name_env}{self.colors.ENDC}`"
        )
        self.create_virtualenv_not_change_dir()
        CreateFileBaseAndUpdate(
            os.path.basename(os.getcwd()), ""
        ).create_setting_vscode()


class InstallModule:
    """Module install module"""

    def __init__(self, arg=None) -> None:
        self.package_name = arg
        self.colors = Colors()
        self.notice = Colors().notice()
        self.commands = Commands()
        self.env_directory = EnvAll().get_env_name()
        self.root_directory = EnvAll().get_root_dir_name()

    def install_required_package(self):
        """
        It checks if the platform is Windows, if it is, it runs the command:

        <code>.\{self.env_directory}\Scripts\python.exe -m pip install
        {self.package_name.install}</code>

        The problem is that it doesn't work
        """
        print(f"{self.notice} Installing {self.package_name.install}")
        try:
            if platform.system() == "Windows":
                os.system(
                    rf".\{self.env_directory}\Scripts\python.exe -m pip install {self.package_name.install}"
                )
                print(
                    f"{self.notice} Successfully installed {self.package_name.install}"
                )
            elif platform.system() == "Linux":
                os.system(
                    f"bash -c 'source {self.env_directory}/bin/activate  && pip install {self.package_name.install}'"
                )
                print(
                    f"{self.notice} Successfully installed {self.package_name.install}"
                )
        except TimeoutError as e:
            print(e)

    def add_module_to_txt(self):
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
        if self.env_directory:
            if platform.system() == "Windows":
                os.system(
                    f".\{self.env_directory}\Scripts\python.exe -m pip freeze > requirements.txt"
                )
            elif platform.system() == "Linux":
                os.system(
                    f"bash -c 'source {self.env_directory}/bin/activate  && pip freeze > requirements.txt'"
                )
            print(
                self.notice
                + f'Successfully module {self.package_name.install} added to "requirements.txt"'
            )

    def install_package_only(self):
        """
        It tries to install a package, if it fails, it prints a message

        Args:
        args (str): The arguments passed to the command.
        Example:
            ```py
            install_package_only("package_name")
            ```
        Return:
            None
        """
        try:
            if self.env_directory:
                self.install_required_package()
                self.add_module_to_txt()
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
                        OnlyVirtualEnv().run_process()
                        folder_name = "env*"
                        folder_name_env = str(
                            fnmatch.filter(os.listdir("."), folder_name)[0]
                        )
                        self.install_required_package()
                        break
                    elif response.lower() == "n":
                        self.install_required_package()
                        break
        except AttributeError as err:
            print(
                self.colors.LIGHTGREEN_EX
                + "An error was encountered, it could not be installed."
                + self.colors.ENDC
            )

    def install_package_all(self):
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
            elif platform.system() == "Linux":
                os.system(
                    f"bash -c 'source {folder_name_env}/bin/activate && pip install -r requirements.txt'"
                )

        def run_install_main(folder_name_env):
            if folder_name_env:
                print(
                    f"Found directory  `{self.colors.LIGHTGREEN_EX}{folder_name_env}{self.colors.ENDC}`"
                )
                print(
                    f"Installing modules with  `{self.colors.LIGHTGREEN_EX}{folder_name_env}{self.colors.ENDC}`"
                )
                install_package_follow_env(folder_name_env)
                print(
                    self.notice
                    + f'Successfully installed module from "requirements.txt"'
                )
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
                        OnlyVirtualEnv().run_process()
                        folder_name = "env*"
                        folder_name_env = str(
                            fnmatch.filter(os.listdir("."), folder_name)[0]
                        )
                        print(
                            f"Installing modules with  `{self.colors.LIGHTGREEN_EX}{folder_name_env}{self.colors.ENDC}`"
                        )
                        install_package_follow_env(folder_name_env)
                        print(
                            self.notice
                            + f'Successfully installed modules from "requirements.txt"'
                        )
                        break
                    elif response.lower() == "n":
                        os.system(f"pip install -r requirements.txt")
                        break

        if requirements_file in os.listdir("."):
            run_install_main(folder_name_env)
        else:
            print(
                f"Maybe you forgot to put the name of the package to ininstall? for example `{self.colors.LIGHTGREEN_EX}fenv ininstall{self.colors.OKBLUE} <package_name>{self.colors.ENDC}` \nOr you can use `{self.colors.LIGHTGREEN_EX}fenv ininstall{self.colors.ENDC}` alone. But there must be {self.colors.FAIL}{requirements_file}{self.colors.ENDC} in the current directory"
            )


class UninstallModule:
    def __init__(self, arg) -> None:
        self.package_name = arg
        self.colors = Colors()
        self.notice = Colors().notice()
        self.commands = Commands()
        self.env_directory = EnvAll().get_env_name()
        self.root_directory = EnvAll().get_root_dir_name()

    def cmd_uninstall_package(self):
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
                    f".\{self.env_directory}\Scripts\python.exe -m pip uninstall {self.package_name.uninstall}"
                )
            elif platform.system() == "Linux":
                os.system(
                    f"bash -c 'source {self.env_directory}/bin/activate && pip uninstall {self.package_name.uninstall} -y'"
                )
            print(
                self.notice
                + f"Successfully uninstalled module {self.package_name.uninstall}"
            )
        except TimeoutError:
            print(TimeoutError)

    def remove_module_exit_txt(self):
        try:
            os.system(f"pip freeze > requirements.txt")
            print(
                self.notice
                + f'Successfully uninstalled module {self.package_name.uninstall} exit from "requirements.txt"'
            )
        except Exception as e:
            print(f"Error: {e}")

    def process_run(self):
        """
        "A function that is called when the user runs the command "uninstall"."

        The first line of the function is a docstring. It's a string that describes what the function does.
        It's a good idea to include a docstring for every function you write

        Args:
        args (str): The arguments passed to the command
        Example:
            ```py
            process_run("package_name")
            ```
        Return:
            None
        """
        try:
            print(self.notice + "Uninstalling...")
            self.cmd_uninstall_package()
            self.remove_module_exit_txt()
        except AttributeError as err:
            print(err, "An error was encountered, it could not be uninstalled.")


class Cleanup:
    def __init__(self) -> None:
        pass

    def run_process(self):
        print("😵Cominig Soon...")
