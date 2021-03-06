#!/usr/bin/env python
"""The setup script."""
from setuptools import setup

with open("./README.md", "r") as handle:
    readme_text = handle.read()

with open("./requirements_dev.txt", "r") as handle:
    requirements_dev = [lv.strip() for lv in handle.read().splitlines() if lv.strip()]

with open("./requirements_doc.txt", "r") as handle:
    requirements_doc = [ld.strip() for ld in handle.read().splitlines() if ld.strip()]

setup(
    name="python-pkg-cookiecutter",
    version="0.1.0",
    description="A cookie cutter package for creating python packages.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Chris Sewell",
    author_email="chrisj_sewell@hotmail.com",
    url="https://github.com/executablebooks/python-pkg-cookiecutter",
    license="MIT",
    packages=[],
    install_requires=[],
    extras_require={
        "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
        "testing": requirements_dev,
        "docs": requirements_doc,
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="cookiecutter python",
)
