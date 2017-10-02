import pytest
from run import *
from flask import current_app



def test_check():
    #assert 1+1==2
    with app.app_context():
        assert check_stock("test") == False
        #assert check_stock("gld") == True
        assert count() == 8
