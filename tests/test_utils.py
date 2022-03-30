
#this is the "test/test_utils.py" file ...

from app.utils import to_usd


#def test_answer():
#        assert to_usd(3) == 5

def test_to_usd():
    #it rounds to two decimals places (and adds dollar sign)
    assert to_usd(0.455555) == "$0.46"
    #for large number, adds thousands sparator
    assert to_usd(123456789.98) == "$123,456,789.98"
