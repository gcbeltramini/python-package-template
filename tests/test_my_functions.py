from my_package import my_functions


def test_foo():
    result: int = my_functions.foo(3)
    expected: int = 4
    assert result == expected
