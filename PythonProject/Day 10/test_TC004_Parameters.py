import pytest

@pytest.mark.parametrize("a,b,res",[(1,2,3),(3,4,7)])
def test_add(a,b,res):
        assert a+b==res
        print(a+b)
        assert a+b==res

@pytest.mark.smoke
def test_smoke():
    assert True
    
@pytest.mark.skip(reason="Not Ready")
def test_skip():
    pass