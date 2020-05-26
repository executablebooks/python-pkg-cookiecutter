# python-pkg-cookiecutter

[![Code style: black][black-badge]][black-link]

A cookie cutter package for creating python packages with all the mod-cons:

- pre-commit checks with flake8 and black
- pytest setup
- github actions for pre-commit, pytest and pypi deployment

## Notes

PyPi deployment requires a PyPI API key to be added to the GitHub repo's secrets (named `PYPI_KEY`)

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
