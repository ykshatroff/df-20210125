import os
from unittest.mock import patch, Mock

import pytest

from hello import hello, Hello, User


def test_hello():
    assert hello() == "Hello world, asdf"


@patch.object(os, 'environ')
def test_hello_user(mock):
    assert hello() == f"Hello world, user"


def test_hello_bad():
    assert hello() == "Hello world, asdf"


def test_mock():
    mock = Mock()
    assert isinstance(mock.attribute, Mock)
    assert isinstance(mock.attribute.subattribute, Mock)
    assert isinstance(mock.method().subattribute, Mock)
    assert isinstance(mock.method().subattribute(), Mock)


def test_class_hello():
    assert User("user").get_name() == 'user'
    with patch.object(os, 'environ', {"SECRET": 'user'}):
        assert Hello().output() == f"Hello world, user"

    hello_object = Hello()
    with patch.object(hello_object, 'get_user') as mock_user:
        mock_user.return_value = User("NOT USER")
        assert hello_object.output() == f"Hello world, NOT USER"

    with patch.object(hello_object, 'get_user') as mock_user:
        mock_user.side_effect = ValueError("Bad user")

        with pytest.raises(ValueError) as error:
            hello_object.output()

        assert error.match("Bad user")
        assert isinstance(error.value, ValueError)

