import os

import pytest

from hello import hello


@pytest.fixture()
def os_environ_user():
    old_env = os.environ['SECRET']
    user = 'user'
    os.environ['SECRET'] = user
    yield user
    # wrap up
    os.environ['SECRET'] = old_env


def test_hello():
    assert hello() == "Hello world, asdf"


def test_hello_user(os_environ_user):
    assert hello() == f"Hello world, {os_environ_user}"


def test_hello_bad():
    assert hello() == "Hello world, asdf"
