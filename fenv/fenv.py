version: str = '0.0.12.1'
""" Module fenv main """
from fenv.customizes.colors import Colors
from fenv.assets.commands import Commands
from fenv.env_all import EnvAll
from fenv.manage_file import (
    CreateFileBaseAndUpdate,
    OnlyVirtualEnv,
    InstallModule,
    UninstallModule,
    Cleanup,
)
from fenv.state_env import StateEnv

from argparse import ArgumentParser
import os

colors = Colors()
notice = colors.notice()

env_above = EnvAll()
env_directory = env_above.get_env_name()
root_directory = env_above.get_root_dir_name()


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
        usage=f"{colors.NAVY}fenv install {colors.NAVY}<package_name>{colors.ENDC} or {colors.HOT_PINK}fenv install {colors.ENDC}",
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
        usage=f"{colors.HOT_PINK}fenv uninstall <package_name>{colors.ENDC}",
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
        usage=f"{colors.HOT_PINK}fenv update{colors.ENDC}",
    )

    onlyenv_cmd = subparsers.add_parser(
        "onlyenv",
        help="Create only virtualenv and no create base file",
        usage=f"{colors.HOT_PINK}fenv onlyenv{colors.ENDC}",
    )

    clean_cmd = subparsers.add_parser(
        "clean", help="Clean delete all packages in requirements.txt out"
    )
    activate_cmd = subparsers.add_parser(
        "activate", help="Command hint to activate virtual environment with folder"
    )
    deactivate_cmd = subparsers.add_parser(
        "deactivate", help="Command hint to deactivate virtual environment with folder"
    )
    test_cmd = subparsers.add_parser("test", help="test")

    general_group = parser.add_argument_group(title="General Options")
    general_group.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit"
    )
    general_group.add_argument(
        "-v", "--version", action="store_true", help="check version fenv"
    )

    return parser.parse_args()


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
        try:
            CreateFileBaseAndUpdate(args.new, "create").procress_only_create_project()
        except TypeError as err:
            print(
                f"Maybe you forgot to enter the name of the folder? For example: {colors.LIGHTGREEN_EX}fenv new{colors.NAVY} <project_folder>{colors.ENDC}"
            )

    elif args.__dict__["command"] == "install":
        InstallModule(
            args
        ).install_package_only() if args.install != None else InstallModule(
            args
        ).install_package_all()

    elif args.__dict__["command"] == "uninstall":
        UninstallModule(args).process_run() if args.uninstall != None else print(
            f"Maybe you forgot to put the name of the package to uninstall? "
            f"For example: {colors.LIGHTGREEN_EX}fenv uninstall{colors.OKBLUE} <package_name>{colors.ENDC}"
        )
    elif args.__dict__["command"] == "update":
        CreateFileBaseAndUpdate(
            root_directory, "update"
        ).process_create_base_file_and_update()
        print(f"{notice}Updated tree path to readme.md")
        os.system("pip freeze > requirements.txt")
        print(f"{notice}Updated module all to requirements.txt")
    elif args.__dict__["command"] == "onlyenv":
        OnlyVirtualEnv().run_process()

    elif args.__dict__["command"] == "clean":
        question = input(
            "Do you want to delete all packages in requirements.txt out? (y/n) "
        ).lower()
        if question in ["y", ""]:
            Cleanup().remove_lib_not_default_in_env()
    elif args.__dict__["command"] == "activate":
        StateEnv().activate()
    elif args.__dict__["command"] == "test":
        print("D:D:D:D:D:D:D:D")


def main():
    """
    It takes the arguments from the command line and passes them to the create_project_all function
    Return:
        None
    """
    args = setup_parse()

    print(
        f"⏩ {colors.LIGHTMAGENTA_EX}Hello,Fenv {colors.POWDER_BLUE}[{colors.MINT_GREEN}v{version}{colors.POWDER_BLUE}]{colors.ENDC}🫡\n".center(
            40, "-"
        )
    ) if args.__dict__["command"] is None else None
    check_command(args)
