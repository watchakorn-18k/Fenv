from setuptools import setup, find_packages
from dotenv import load_dotenv

load_dotenv()
import codecs
import os

new_version = os.getenv("FENV_VERSION")
file_path = f"{os.path.abspath(os.path.dirname(__file__))}/fenv/fenv.py"

# Read the original content of the file
with open(file_path, "r", encoding="utf-8") as file:
    original_content = file.readlines()

# Modify the first line of the file with the new version string
modified_content = [f"version: str = '{new_version}'\n"] + original_content[1:]

# Write the modified content back to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.writelines(modified_content)

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = os.getenv("FENV_VERSION")
DESCRIPTION = (
    "Generate a folder, establish a virtual environment with a single command."
)
LONG_DESCRIPTION = "Generate a folder, establish a virtual environment, and simultaneously create the essential basic Python files, all with a single command"

# Setting up
setup(
    name="Fenv",
    version=VERSION,
    author="wk18k (watchakorn-18k)",
    author_email="<porton555@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["virtualenv"],
    entry_points="""
    [console_scripts]
    fenv=fenv.fenv:main
    """,
    keywords=["python", "virtualenv", "create file", "create folder", "fenv", "wk-18k"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
)
