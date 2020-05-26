import {{ cookiecutter.package_name }}


def test_version():
    assert isinstance({{ cookiecutter.package_name }}.__version__, str)
