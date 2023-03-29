from setuptools import setup, find_packages
from dotenv import load_dotenv

load_dotenv()
import codecs
import os

a = 1
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
