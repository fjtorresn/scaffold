from hello import toyou, add, subtract


def test_hello_subtract():
    assert subtract(10) == 9


def test_hello_add():
    assert add(7) == 8


def test_hello_toyou():
    assert toyou("Francisco") == "hi Francisco"
