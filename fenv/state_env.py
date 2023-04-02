""" Module for open a virtual environment and clsoe the virtual environment """


from fenv.env_all import EnvAll
from fenv.customizes.colors import Colors

import os

ENV_NAME = EnvAll().get_env_name()
colors = Colors()

path_env_win, os_win = EnvAll().get_path_env_for_windows()
path_env_linux, os_linux = EnvAll().get_path_env_for_linux()


class StateEnv:
    def activate(self):
        """
        If the environment name is not empty, then if the operating system is Windows, then if the
        operating system is Windows and the terminal is xterm-256color, then print the message
        """

        if ENV_NAME:
            if os_win:
                if os_win and os.environ.get("TERM") == "xterm-256color":
                    print(
                        f"It cannot be enabled, but you can run it using the \n `{colors.NAVY}source {colors.SPRING_GREEN}{ENV_NAME}/Scripts/activate{colors.ENDC}` command"
                    )

                elif os_win and EnvAll().get_terminal_prompt():
                    print(
                        f"It cannot be enabled, but you can run it using the \n {colors.SPRING_GREEN}`{ENV_NAME}\\Scripts\\activate.bat`{colors.ENDC} command"
                    )
                else:
                    print(
                        f"It cannot be enabled, but you can run it using the \n {colors.SPRING_GREEN}`{ENV_NAME}\\Scripts\\activate.bat`{colors.ENDC} command"
                    )
            elif os_linux:
                if EnvAll().get_terminal_bash():
                    print(
                        f"It cannot be enabled, but you can run it using the \n `{colors.NAVY}source {colors.SPRING_GREEN}{ENV_NAME}/bin/activate{colors.ENDC}` command"
                    )
        else:
            print("The virtual environment was not found when creating it with fenv.")

    def deactivate(self):
        """
        If the environment is found, it will print a message to the user that it cannot be enabled, but
        it can be run using the `deactivate` command
        """
        if ENV_NAME:
            if os_win:
                if os_win and os.environ.get("TERM") == "xterm-256color":
                    print(
                        f"It cannot be enabled, but you can run it using the \n `{colors.NAVY}{colors.SPRING_GREEN}deactivate{colors.ENDC}` command"
                    )

                elif os_win and EnvAll().get_terminal_prompt():
                    print(
                        f"It cannot be enabled, but you can run it using the \n {colors.SPRING_GREEN}`{ENV_NAME}\\Scripts\\deactivate.bat`{colors.ENDC} command"
                    )

                # os.system(rf".\{path_env_win}\activate")
            elif os_linux:
                if EnvAll().get_terminal_bash():
                    print(
                        f"It cannot be enabled, but you can run it using the \n `{colors.NAVY}{colors.SPRING_GREEN}deactivate{colors.ENDC}` command"
                    )
        else:
            print("The virtual environment was not found when creating it with fenv.")
