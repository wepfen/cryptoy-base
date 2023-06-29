from cryptoy.tp import (
    hello_tp,
)


def test_hello_tp() -> None:
    assert hello_tp() == "hello_tp"
