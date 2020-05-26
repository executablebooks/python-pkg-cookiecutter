#!/usr/bin/env python
"""The setup script."""
from setuptools import setup, find_packages

with open("{{ cookiecutter.package_name }}/__init__.py", "r") as handle:
    for line in handle:
        if "__version__" in line:
            version = line.split(" = ")[-1].strip('"')
            break

with open("./README.md", "r") as handle:
    readme_text = handle.read()

with open("./requirements.txt", "r") as handle:
    requirements = [l.strip() for l in handle.read().splitlines() if l.strip()]

with open("./requirements_dev.txt", "r") as handle:
    requirements_dev = [l.strip() for l in handle.read().splitlines() if l.strip()]

with open("./requirements_doc.txt", "r") as handle:
    requirements_doc = [l.strip() for l in handle.read().splitlines() if l.strip()]

setup(
    name="{{ cookiecutter.project_name }}",
    version=version,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.owner }}",
    author_email="{{ cookiecutter.email }}",
    url=(
        "https://github.com/"
        "{{ cookiecutter.github_basename }}/{{ cookiecutter.project_name }}"
    ),
    license="MIT",
    packages=find_packages(),
    install_requires=requirements,
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
    keywords="",
)
