""" Module about passing folder names """
import fnmatch
import os
import configparser
import platform
import glob


class EnvAll:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.config = configparser.ConfigParser()

    def get_env_name(self):
        """It's a function that checks if the environment directory exists.
        Return:
            [] : empyt list
        """
        self.folder_name = "env_*"
        return (
            fnmatch.filter(os.listdir("."), self.folder_name)
            if fnmatch.filter(os.listdir("."), self.folder_name) == []
            else str(fnmatch.filter(os.listdir("."), self.folder_name)[0])
        )

    def get_root_dir_name(self):
        """It's a function that checks if the root directory exists.

        Return:
            str : root directory
        """
        return os.path.basename(os.path.abspath("."))

    def create_lib_default_env(self):
        """It's a function that creates the env.
        Return:
            str : env name
        """
        self.data_list = []

        if platform.system() == "Windows":
            path_lib_all = self.get_path_lib_all()
            for i in os.listdir(path_lib_all):
                self.data_list.append(i)
                self.data_string = ",".join(self.data_list)
                self.config["fenv"] = {"default_lib": self.data_string}
                with open(rf"{self.get_env_name()}\fenv.cfg", "w") as configfile:
                    self.config.write(configfile)
        elif platform.system() == "Linux":
            path_lib_all = self.get_path_lib_all()
            for i in os.listdir(path_lib_all):
                self.data_list.append(i)
                self.data_string = ",".join(self.data_list)
                self.config["fenv"] = {
                    "default_lib": self.data_string,
                }
                with open(rf"{self.get_env_name()}/fenv.cfg", "w") as configfile:
                    self.config.write(configfile)

    def get_lib_default_env(self):
        """
        It reads a config file, gets a string, splits it into a list, and returns the list
        Return:
            data_list : list
        """
        self.config.read(rf"{self.get_env_name()}/fenv.cfg")

        self.data_string = self.config.get("fenv", "default_lib")

        self.data_list = self.data_string.split(",")
        return self.data_list

    def get_path_lib_all(self):
        """
        It's a function that checks if the environment directory exists.
        Return:
            path_lib_all : str
        """
        if platform.system() == "Windows":
            return f"{self.get_env_name()}\Lib\site-packages"
        elif platform.system() == "Linux":
            return "".join(
                glob.glob(f"{self.get_env_name()}/lib/python*/site-packages")
            )

    def get_path_env_for_windows(self):
        if platform.system() == "Windows":
            return rf"{self.get_env_name()}\Scripts", "Windows"
        else:
            return None, None

    def get_path_env_for_linux(self):
        if platform.system() == "Linux":
            return rf"{self.get_env_name()}/bin", "Linux"
        else:
            return None, None

    def get_terminal_prompt(self):
        try:
            return len(os.environ.get("PROMPT")) == 10
        except Exception:
            pass

    def get_terminal_bash(self):
        return "xterm" in os.environ.get("TERM") or "gnome-terminal" in os.environ.get(
            "TERM"
        )
