""" Module about passing folder names """
import fnmatch
import os


class EnvAll:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

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
