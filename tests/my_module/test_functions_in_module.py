from my_package.my_module import functions_in_module


def test_bar():
    result: int = functions_in_module.bar(3)
    expected: int = 6
    assert result == expected
