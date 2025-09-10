from app.app import myfunction

def test_myfunction_returns_type_str():
    assert isinstance(myfunction(), str)

def test_myfunction_is_not_empty():
    assert myfunction() != ""

def test_myfunction_is_exact_phrase():
    assert myfunction() == "Hello, World!"

