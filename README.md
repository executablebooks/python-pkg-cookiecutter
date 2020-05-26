# python-pkg-cookiecutter

[![Code style: black][black-badge]][black-link]

A cookie cutter package for creating python packages with all the mod-cons:

- pre-commit checks with flake8 (linting) and black (formatting)
- pytest setup
- github actions for pre-commit, pytest and (optional) PyPi deployment
- sphinx docs builds
- Circle CI for documentation testing
- github issues templates

See [tests/test_bake/test_bake_with_defaults.yml](https://github.com/executablebooks/python-pkg-cookiecutter/blob/master/tests/test_bake/test_bake_with_defaults.yml),
for the list of created files.

## Usage

```console
$ pip install cookiecutter  # tested with cookiecutter==1.6
$ cookiecutter https://github.com/executablebooks/python-pkg-cookiecutter.git
```

Enter created folder then run tests:

```
$ pip install -e .[code_style,testing]
$ flake8 .
$ black .
$ pytest
```

To use pre-commit, the package must be in a git repository

```
$ git init
$ git add *
# to apply to staged files
$ pre-commit run
# restage if changes
$ git add *
# to run on commits
$ pre-commit install
$ git commit -m 'Initial commit'
```

## Notes

PyPi deployment requires a [PyPI API token](https://pypi.org/help/#apitoken) to be added to the [GitHub secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) (named `PYPI_KEY`).
It is setup to deploy on tagged commits (if tests pass).

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
