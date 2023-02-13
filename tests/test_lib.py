from services_test2 import lib


def test_hello_world() -> None:
    input_msg = "hello world"
    actual = lib.hello_world(input_msg)
    expected = "HELLO WORLD"
    assert actual == expected


def test_send_message() -> None:
    instance = lib.World()
    input_msg = "hello world"
    actual = instance.send_message(input_msg)
    expected = "HELLO WORLD"
    assert actual == expected
