""" Code module for generating content files """


class Commands:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

    def get_main_py(self):
        return """
def main():
    pass


if __name__ == "__main__":
    main()
        """

    def get_main_py(self):
        return """
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Version: {}".format(os.environ("VERSION")))


if __name__ == "__main__":
    main()
        """

    def get_readme_md(self):
        return """
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://cdn.discordapp.com/attachments/585069498986397707/1112788994175012936/image-removebg-preview.png">
  <img src="https://cdn.discordapp.com/attachments/585069498986397707/1112788501642104832/OIG.png">
</picture>

<h1 align="center">{}</h1>
<p align="center">A brief and descriptive title for your project.</p>

<p align="center">
  <a href="LICENSE" target="_blank">
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" />
  </a>
  <a href="LICENSE" target="_blank">
    <img alt="Python" src="https://img.shields.io/badge/version-{}-gree?style=for-the-badge&logoColor=white&logo=Python" />
  </a>

</p>

## Description

A detailed description of the project, including its purpose, features, and any other relevant information.

## Getting Started

```
git clone https://github.com/{}/{}.git

cd {}

```

## Installation

```
# create virtualenv auto name
fenv env

# install package in requirements.txt
fenv install

# Or use pip
pip install -r requirements.txt

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

    def get_requirements_txt(self):
        return """
black
fenv
python-dotenv
"""

    def get_update_tree_path(self):
        return """
<!--- Start Tree --->
```bash
.
└── {}/
{}
```
"""
