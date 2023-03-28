""" Module about passing folder names """
import fnmatch
import os
import configparser


class EnvAll:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.config = configparser.ConfigParser()

    def get_env_name(self):
        """It's a function that checks if the environment directory exists.
        Return:
            [] : empyt list
        """
        self.folder_name = "env*"
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
        print(self.get_env_name())
        for i in os.listdir(f"{self.get_env_name()}\Lib\site-packages"):
            self.data_list.append(i)

        self.data_string = ",".join(self.data_list)

        self.config["fenv"] = {"default_lib": self.data_string}

        with open(rf"{self.get_env_name()}\fenv.cfg", "w") as configfile:
            self.config.write(configfile)

    def get_lib_default_env(self):
        self.config.read("example.cfg")

        self.data_string = self.config.get("fenv", "default_lib")

        self.data_list = self.data_string.split(",")
        return self.data_list
