""" Module for open a virtual environment and clsoe the virtual environment """


from fenv.env_all import EnvAll
from fenv.customizes.colors import Colors

import subprocess
import os

ENV_NAME = EnvAll().get_env_name()
colors = Colors()

path_env_win, os_win = EnvAll().get_path_env_for_windows()
path_env_linux, os_linux = EnvAll().get_path_env_for_linux()


class StateEnv:
    def activate(self):
        """Method to activate a virtual environment"""

        IS_POWER_SHELL = len(os.getenv("PSModulePath", "").split(os.pathsep)) >= 3
        IS_LINUX_OR_WSL = os.path.exists("/proc/sys/kernel/osrelease")

        if ENV_NAME:
            if os_win:
                if IS_POWER_SHELL:
                    subprocess.run(
                        [
                            "powershell.exe",
                            "-NoExit",
                            "-Command",
                            rf".\{path_env_win}\activate",
                        ],
                    )
                elif os.environ.get("TERM") == "xterm-256color":
                    subprocess.run(
                        [
                            "cmd.exe",
                            "/c",
                            rf".\{path_env_win}\activate.bat",
                        ]
                    )
                else:
                    print(
                        f"It cannot be enabled, but you can run it using the \n {colors.SPRING_GREEN}`{ENV_NAME}\\Scripts\\activate`{colors.ENDC} command"
                    )

            elif os_linux:
                if EnvAll().get_terminal_bash():
                    if IS_LINUX_OR_WSL:
                        subprocess.run(
                            [
                                "bash.exe",
                                "-c",
                                rf".\{path_env_win}\activate",
                            ],
                        )
                        print(
                            f"Virtual environment {colors.NAVY}{colors.SPRING_GREEN}{ENV_NAME}{colors.ENDC} is enabled"
                        )
                    else:
                        subprocess.run(
                            [
                                "bash",
                                "-c",
                                rf".\{path_env_win}\activate",
                            ],
                        )
                        print(
                            f"Virtual environment {colors.NAVY}{colors.SPRING_GREEN}{ENV_NAME}{colors.ENDC} is enabled"
                        )
        else:
            print(
                f"Virtual environment {colors.NAVY}{colors.SPRING_GREEN}{ENV_NAME}{colors.ENDC} is not enabled because it does not exist"
            )
