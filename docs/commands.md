```py
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
def main():
    pass


if __name__ == "__main__":
    main()
        """

    def get_readme_md(self):
        return """
```

```
# {}
A brief and descriptive title for your project.

## Description

A detailed description of the project, including its purpose, features, and any other relevant information.

## Getting Started

```

```

git clone https://github.com/<User Name Github>/{}.git

cd {}

```

```

## Installation

```

```

# create virtualenv auto name

fenv env

# install package in requirements.txt

fenv install

```

```

## Usage

Instructions on how to use the project, including any usage examples and screenshots.

## Tree
<!--- Start Tree --->
```

```bash
.
└── {}/
{}
```

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
"""
```

```

    def get_update_tree_path(self):
        return """

<!--- Start Tree --->
```

```bash
.
└── {}/
{}
```

```
"""
```
