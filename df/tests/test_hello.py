import os
from unittest.mock import patch

import pytest

from hello import hello


@pytest.fixture()
def os_environ_user():
    user = 'user'
    with patch.object(os, 'environ', {'SECRET': user}):
        yield user
    # wrap up


def test_hello():
    assert hello() == "Hello world, asdf"


def test_hello_user(os_environ_user):
    assert hello() == f"Hello world, {os_environ_user}"


def test_hello_bad():
    assert hello() == "Hello world, asdf"
