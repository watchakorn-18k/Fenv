""" Module manage create file """
import os
import shutil
import subprocess
import platform
import re
import random
import fnmatch
import urllib.request

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
        print(
            f'{self.notice}Successfully created the file {self.colors.HOT_PINK}"{self.file_path}"{self.colors.ENDC}'
        )

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
        print(
            f'{self.notice}Successfully created the file {self.colors.HOT_PINK}"{markdown_path}"{self.colors.ENDC}'
        )

    def create_file_freeze(self):
        """
        It creates a file called "requirements.txt" and writes the string "black" to it
        """
        module_base = self.commands.get_requirements_txt()
        with open("requirements.txt", "w") as f:
            f.write(module_base)
        os.chmod("requirements.txt", 0o777)
        print(
            f'{self.notice}Successfully created the file {self.colors.HOT_PINK}"requirements.txt"{self.colors.ENDC}'
        )

    def create_file_gitignore(self):
        """
        It creates a file called .gitignore and writes the string "*.pyc" to it
        """
        with open(".gitignore", "w") as f:
            f.write(f"*.pyc\n/{self.env_directory}")
        os.chmod(".gitignore", 0o777)
        print(
            f'{self.notice}Successfully created the file {self.colors.HOT_PINK}".gitignore"{self.colors.ENDC}'
        )

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
            print(
                f"{self.notice}creating virtualenv {self.colors.HOT_PINK}env_{self.name}...{self.colors.ENDC}"
            )
            os.system(f"virtualenv env_{self.name}")
            EnvAll().create_lib_default_env()
        print(
            f'{self.notice}Successfully created the virtualenv {self.colors.HOT_PINK}"{self.name}"{self.colors.ENDC}'
        )

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
        print(
            f'{self.notice}Successfully created the {self.colors.HOT_PINK}".vscode/settings.json"{self.colors.ENDC}'
        )

    def run_install_module_base(self):
        """
        It installs the base Python modules

        :param env: The environment object
        """

        if platform.system() == "Windows":
            self._extracted_from_run_install_module_base_9(
                ".\env_",
                "\Scripts\python.exe -m pip install -r requirements.txt",
                "\Scripts\python.exe -m pip freeze > requirements.txt",
                "\Scripts\python.exe -m pip install --upgrade pip",
            )
        elif platform.system() == "Linux":
            self._extracted_from_run_install_module_base_9(
                "bash -c 'source env_",
                "/bin/activate  && pip install -r requirements.txt'",
                "/bin/activate  && pip freeze > requirements.txt'",
                "/bin/activate  && pip install --upgrade pip'",
            )

    # TODO Rename this here and in `run_install_module_base`
    def _extracted_from_run_install_module_base_9(self, arg0, arg1, arg2, arg3):
        os.system(f"{arg0}{self.name}{arg1}")
        print(
            f'{self.notice}Successfully installed module in {self.colors.HOT_PINK}"requirements.txt"{self.colors.ENDC}'
        )
        os.system(f"{arg0}{self.name}{arg2}")
        print(
            f'{self.notice}Successfully updated the file {self.colors.HOT_PINK}"requirements.txt"{self.colors.ENDC}'
        )
        os.system(f"{arg0}{self.name}{arg3}")

    def create_folder(self):
        """
        It creates a folder with the name of the argument passed to it

        Example:
            ```py
            create_folder("project_name")
            ```
        Return:
            1 : if has folder already
        """
        try:
            os.mkdir(self.name)
            global is_has_folder
            is_has_folder = False
        except FileExistsError:
            print(
                f"{self.notice} Project: {self.colors.PALE_GREEN}{self.name}{self.colors.ENDC} already exists"
            )
            is_has_folder = True
            return 1
        else:
            print(
                f'{self.notice}Successfully created the directory {self.colors.HOT_PINK}"{self.name}"{self.colors.ENDC}'
            )

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

    def random_name_project(self) -> str:
        list_name = [f"Samai{random.randint(00,99)}", f"Danai{random.randint(00,99)}"]
        return random.choice(list_name)

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
            return f"{self.name[:10]}"
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

        print(f'{self.notice}Successfully created the virtualenv "{self._name_env}"')

    def run_process(self):
        """
        It creates a virtual environment and a vscode settings file.
        """
        self._name_env = self.create_name_env()
        print(
            f"your env name is `{self.colors.MINT_GREEN}{self._name_env}{self.colors.ENDC}`"
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
        print(
            f"{self.notice} Installing {self.colors.PURPLE}{self.package_name.install}{self.colors.ENDC}{self.colors.SEA_GREEN}"
        )
        if platform.system() == "Windows":
            try:
                subprocess.check_call(
                    [
                        rf".\{self.env_directory}\Scripts\python.exe",
                        "-m",
                        "pip",
                        "install",
                        self.package_name.install,
                    ]
                )
                print(
                    f"{self.notice}Successfully installed {self.colors.PURPLE}{self.package_name.install}{self.colors.ENDC}"
                )
            except subprocess.CalledProcessError as e:
                error_msg = str(e.output)
                if "ERROR: Could not find a version" in error_msg:
                    print(
                        f"{self.notice} Could not find a version of {self.package_name.install} to install."
                    )
                else:
                    print(
                        f"{self.notice} Failed to install {self.colors.PURPLE}{self.package_name.install}{self.colors.ENDC} Error message: {self.colors.RED}{error_msg}{self.colors.ENDC}"
                    )

        elif platform.system() == "Linux":
            try:
                subprocess.check_call(
                    [
                        "/bin/bash",
                        "-c",
                        f"source {self.env_directory}/bin/activate && pip install {self.package_name.install}",
                    ]
                )
                print(
                    f"{self.notice}Successfully installed {self.colors.PURPLE}{self.package_name.install}{self.colors.ENDC}"
                )
            except subprocess.CalledProcessError as e:
                error_msg = str(e.output)
                if "ERROR: Could not find a version" in error_msg:
                    print(
                        f"{self.notice} Could not find a version of {self.package_name.install} to install."
                    )
                else:
                    print(
                        f"{self.notice} Failed to install {self.colors.PURPLE}{self.package_name.install}{self.colors.ENDC} Error message: {self.colors.RED}{error_msg}{self.colors.ENDC}"
                    )

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
                + f'Successfully module {self.colors.PURPLE}{self.package_name.install}{self.colors.ENDC} added to "{self.colors.SEA_GREEN}requirements.txt{self.colors.ENDC}"'
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
                    if response.lower() in ["y", "yes", ""]:
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
                self.colors.SPRING_GREEN
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
                    f"Found directory  `{self.colors.SPRING_GREEN}{folder_name_env}{self.colors.ENDC}`"
                )
                print(
                    f"Installing modules with  `{self.colors.SPRING_GREEN}{folder_name_env}{self.colors.ENDC}`"
                )
                install_package_follow_env(folder_name_env)
                print(
                    f'{self.notice}Successfully installed module from {self.colors.SPRING_GREEN}"requirements.txt"{self.colors.ENDC}'
                )
            else:
                while True:
                    response = input(
                        "We couldn't find the fenv virtual environment. Would you like to set up a new one? (y/n): "
                    )
                    if response.lower() in ["y", "yes", ""]:
                        OnlyVirtualEnv().run_process()
                        folder_name = "env*"
                        folder_name_env = str(
                            fnmatch.filter(os.listdir("."), folder_name)[0]
                        )
                        print(
                            f"Installing modules with  `{self.colors.SPRING_GREEN}{folder_name_env}{self.colors.ENDC}`"
                        )
                        install_package_follow_env(folder_name_env)
                        print(
                            f'{self.notice}Successfully installed modules from "requirements.txt"'
                        )
                        break
                    elif response.lower() == "n":
                        os.system("pip install -r requirements.txt")
                        break

        if requirements_file in os.listdir("."):
            run_install_main(folder_name_env)
        else:
            print(
                f"Maybe you forgot to put the name of the package to install? for example `{self.colors.MINT_GREEN}fenv install{self.colors.OKBLUE} <package_name>{self.colors.ENDC}` \nOr you can use `{self.colors.MINT_GREEN}fenv install{self.colors.ENDC}` alone. But there must be {self.colors.FAIL}{requirements_file}{self.colors.ENDC} in the current directory"
            )

    def install_package_from_list(self, data: list, project_name: str):
        if not is_has_folder:
            self.data = data
            try:
                if self.env_directory:
                    self.data = self.data[0].strip("[]").split(",")
                    for i in self.data:
                        self.package_name.install = i
                        self.install_required_package()
                    print(
                        f"{self.notice} Successfully installed {self.colors.SKY_BLUE}{project_name}{self.colors.ENDC}"
                    )
            #                     beautiful_command = """{}
            # ┌───────────────────────────┐
            # │   Open project in VSCode  │
            # ├───────────────────────────┤
            # │                           │
            # │    cd {}{}│
            # │    code .                 │
            # │                           │
            # └───────────────────────────┘
            # Or `cd {} && code .`
            # {}""".format(
            #                         self.colors.MINT_GREEN,
            #                         project_name
            #                         if len(project_name) <= 18
            #                         else f"{project_name[:17]}*",
            #                         " " * abs((18 - len(project_name)) + 2)
            #                         if len(project_name) <= 18
            #                         else " " * 2,
            #                         project_name,
            #                         self.colors.ENDC,
            #                     )

            #                     print(beautiful_command)

            except AttributeError as err:
                print(
                    self.colors.SPRING_GREEN
                    + "An error was encountered, it could not be installed."
                    + self.colors.ENDC
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
            package_dependency_list = self.pip_show_to_dict()["Requires"].split(", ")
            print(f"{self.notice}Uninstalling...{self.colors.ORANGE}")
            if platform.system() == "Windows":
                os.system(
                    f".\{self.env_directory}\Scripts\python.exe -m pip uninstall {self.package_name.uninstall} -y"
                )
                for i in package_dependency_list:
                    os.system(
                        f".\{self.env_directory}\Scripts\python.exe -m pip uninstall {i} -y"
                    )

            elif platform.system() == "Linux":
                os.system(
                    f"bash -c 'source {self.env_directory}/bin/activate && pip uninstall {self.package_name.uninstall} -y'"
                )
                for i in package_dependency_list:
                    os.system(
                        f"bash -c 'source {self.env_directory}/bin/activate && pip uninstall {i} -y'"
                    )
            print(
                self.notice
                + f"Successfully uninstalled module {self.colors.MINT_GREEN}{self.package_name.uninstall}{self.colors.ENDC}"
            )
        except TimeoutError:
            print(TimeoutError)

    def remove_module_exit_txt(self):
        try:
            # os.system(f"pip freeze > requirements.txt")
            if platform.system() == "Windows":
                os.system(
                    f".\{self.env_directory}\Scripts\python.exe -m pip freeze > requirements.txt"
                )
            elif platform.system() == "Linux":
                os.system(
                    f"bash -c 'source {self.env_directory}/bin/activate && pip freeze > requirements.txt'"
                )
            print(
                self.notice
                + f'Successfully uninstalled module {self.colors.MINT_GREEN}{self.package_name.uninstall}{self.colors.ENDC} exit from "{self.colors.ORCHID}requirements.txt{self.colors.ENDC}"'
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
            self.cmd_uninstall_package()
            self.remove_module_exit_txt()
        except AttributeError as err:
            print(err, "An error was encountered, it could not be uninstalled.")

    def pip_show_to_dict(self):
        result = {}
        try:
            # script
            if platform.system() == "Windows":
                output = subprocess.check_output(
                    f".\\{self.env_directory}\\Scripts\\python.exe -m pip show {self.package_name.uninstall}",
                    shell=True,
                ).decode("utf-8")
            elif platform.system() == "Linux":
                output = subprocess.check_output(
                    f"bash -c 'source {self.env_directory}/bin/activate && pip show {self.package_name.uninstall}'",
                    shell=True,
                ).decode("utf-8")
            for line in output.splitlines():
                match = re.match(r"^([^:]+):\s*(.*)$", line)
                if match:
                    key = match[1]
                    value = match[2]
                    result[key] = value
            return result
        except subprocess.CalledProcessError:
            print(
                f"{self.colors.ENDC}You have not installed the {self.colors.ORANGE}{self.package_name.uninstall}{self.colors.ENDC} package."
            )
            exit()


class Cleanup(CreateFileBaseAndUpdate):
    def __init__(self) -> None:
        self.colors = Colors()
        self.notice = Colors().notice()
        self.commands = Commands()
        self.path_lib_all = EnvAll().get_path_lib_all()
        self.lib_default_env = EnvAll().get_lib_default_env()
        self.env_name = EnvAll().get_env_name()

    def remove_lib_not_default_in_env(self):
        """
        Removes all the libraries that are not in the default environment
        """
        data_lib_all = list(os.listdir(self.path_lib_all))
        diff_list_1 = set(data_lib_all) - set(self.lib_default_env)
        diff_list_2 = set(self.lib_default_env) - set(data_lib_all)
        result = diff_list_1.union(diff_list_2)
        os.chdir(self.path_lib_all)
        if len(result) > 0:
            for item in result:
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)
                print(
                    f"{self.notice}{self.colors.SALMON}{item}{self.colors.ENDC} has been removed"
                )
        os.chdir("../../..")
        print(
            f"{self.notice}{self.colors.SKY_BLUE}All the libraries have been removed.{self.colors.ENDC}"
        )
        if platform.system() == "Windows":
            os.system(
                f".\env_{self.env_name }\Scripts\python.exe -m pip freeze > requirements.txt"
            )
            print(
                f'{self.notice}{self.colors.SKY_BLUE}Successfully updated the file "requirements.txt"{self.colors.ENDC}'
            )

        elif platform.system() == "Linux":
            os.system(
                f"bash -c 'source env_{self.env_name }/bin/activate  && pip freeze > requirements.txt'"
            )
            print(
                f'{self.notice}{self.colors.SKY_BLUE}Successfully updated the file "requirements.txt"{self.colors.ENDC}'
            )


class GitCloneVirtualENV:
    def __init__(self, link) -> None:
        self.colors = Colors()
        self.notice = Colors().notice()
        self.commands = Commands()
        self.root_dir = EnvAll().get_root_dir_name()
        self.url = link
        self.name_repo = ""

    def cmd_git_clone(self):
        """
        "A function that is called when the user runs the command "git clone"."
        """
        try:
            subprocess.run(
                [
                    "git",
                    "clone",
                    self.url,
                ]
            )
            self.name_repo = self.url.split("/")[-1]

        except FileNotFoundError:
            print(
                f"The system cannot find the {self.colors.ORANGE}git {self.colors.ENDC}command, can be downloaded at : {self.colors.PURPLE}https://git-scm.com/downloads{self.colors.ENDC}"
            )

    def url_exists(self):
        """
        The function "url_exists" is defined, but its implementation is missing.
        """
        try:
            urllib.request.urlopen(self.url)
            return True
        except urllib.error.HTTPError:
            return False
        except ValueError:
            return False

    def check_file_requirements(self):
        for i in os.listdir("."):
            if i == "requirements.txt":
                break
        if (
            input(
                f"{self.colors.HOT_PINK}In this repository there is a file requirements.txt \n{self.colors.MINT_GREEN}Do you want to install the package contained in the file? [Y/N]: {self.colors.ENDC}"
            ).upper()
            != "N"
        ):
            InstallModule().install_package_all()

    def run_process(self):
        match self.url_exists():
            case True:
                self.cmd_git_clone()
                CreateFileBaseAndUpdate(self.name_repo, "create").create_virtualenv()
                CreateFileBaseAndUpdate(
                    self.name_repo, "create"
                ).create_setting_vscode()
                self.check_file_requirements()
            case False:
                print(
                    "The URL link you entered is invalid, please correct it and try again."
                )
