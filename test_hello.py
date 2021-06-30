from hello import add

def test_add():
    assert 2 == add(1,1)
    assert 3 == add(2,1)
    assert 10 == add(2,8)