import pytest
from run import check_stock

def test_check():
    #assert 1+1==2
    assert check_stock("test") == False
