from greetlab import greet

def test_greet():
    assert greet("Bob") == "Hello, Bob!"

def test_normal_name():
    result = greet("Alice")
    assert result == "Hello, Alice!"

def test_empty_name():
    result = greet("")
    assert result == "Hello, !"
