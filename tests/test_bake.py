from contextlib import contextmanager
import shlex
import os
import pathlib
import subprocess
import datetime
from cookiecutter.utils import rmtree
from pytest_cookies.plugin import Cookies, Result


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies: Cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_bake_with_defaults(cookies: Cookies, data_regression):
    with bake_in_temp_dir(cookies) as result:
        assert result.exception is None, result.exception
        assert result.exit_code == 0, result.exception
        assert result.project.isdir()
        path = pathlib.Path(result._project_dir)
        all_files = [str(p.relative_to(path)) for p in path.glob("**/*")]
        all_files = [p for p in all_files if "__pycache__" not in p]
        data_regression.check({"files": sorted(all_files)})


def test_year_compute_in_license_file(cookies: Cookies):
    with bake_in_temp_dir(cookies) as result:  # type: Result
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_setup_py_file(cookies: Cookies, file_regression):
    with bake_in_temp_dir(cookies) as result:  # type: Result
        content = result.project.join("setup.py").read()
    file_regression.check(content)


def test_bake_and_run_tests(cookies: Cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        run_inside_dir("python setup.py test", str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_withspecialchars_and_run_tests(cookies: Cookies):
    """Ensure that a `full_name` with double quotes does not break setup.py"""
    with bake_in_temp_dir(
        cookies, extra_context={"full_name": 'name "quote" name'}
    ) as result:
        assert result.project.isdir()
        run_inside_dir("python setup.py test", str(result.project)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies: Cookies):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    with bake_in_temp_dir(cookies, extra_context={"full_name": "O'connor"}) as result:
        assert result.project.isdir()
        run_inside_dir("python setup.py test", str(result.project)) == 0


def test_using_pytest(cookies: Cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        # Test the new pytest target
        run_inside_dir("python setup.py pytest", str(result.project)) == 0
