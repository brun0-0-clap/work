def test_normal_list():
    data = ["a","b","c","a"]
    res = set(data)
    assert len(res) == 3

def test_dup_list():
    data = ["x","x","x","x"]
    res = set(data)
    assert len(res) == 1
