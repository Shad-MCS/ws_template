# pylint:disable=C0114
from setuptools import find_packages, setup

setup(
    name="src",
    packages=find_packages(),
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
)
