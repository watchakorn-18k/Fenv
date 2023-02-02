from argparse import ArgumentParser, Namespace
import os
import platform


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


notice = bcolors.OKBLUE + \
    '['+bcolors.ENDC+bcolors.OKGREEN+'notice' + \
    bcolors.OKBLUE + ']' + bcolors.ENDC + " "


def create_dir_file(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def create_virtualenv(virtual_env_name):
    os.chdir(virtual_env_name)
    if not os.path.exists(virtual_env_name):
        try:
            os.system(f"virtualenv env_{virtual_env_name}")
        except EnvironmentError as error:
            print(error)
    print(notice + f'Successfully created the virtualenv "{virtual_env_name}"')


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(notice + f"{folder_name} already exists.")
        return 1
    else:
        print(notice + f'Successfully created the directory "{folder_name}"')


def create_setting_vscode(env_path):
    text_vscode = """{{"python.formatting.provider": "black","python.pythonPath": "{name_env}","editor.formatOnSave": true,}}"""
    create_dir_file(
        '.vscode/settings.json', text_vscode.format(name_env=env_path))
    print(notice + f'Successfully created the .vscode/settings.json')


def create_file_base(name):
    def create_file_main_py():
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
        module_base = """black"""
        with open("requirements.txt", "w") as f:
            f.write(module_base)
        os.chmod("requirements.txt", 0o777)
        print(notice + f'Successfully created the file "requirements.txt"')

    create_file_main_py()
    create_file_readme_md()
    create_file_freeze()


''


def run_install_module_base(env):
    if platform.system() == "Windows":
        os.system(
            f".\env_{env}\Scripts\python.exe -m pip install -r requirements.txt")
        print(notice + f'Successfully installed module in "requirements.txt"')
        os.system(
            f".\env_{env}\Scripts\python.exe -m pip freeze > requirements.txt")
        print(notice + f'Successfully updated the file "requirements.txt"')
        os.system(
            f".\env_{env}\Scripts\python.exe -m pip install --upgrade pip")


def main():
    parser = ArgumentParser()
    parser.add_argument('-new', help="folder name", type=str)
    args: Namespace = parser.parse_args()
    if create_folder(args.name) != 1:
        create_virtualenv(args.name)
        create_setting_vscode(args.name)
        create_file_base(args.name)
        run_install_module_base(args.name)


if __name__ == "__main__":
    main()
