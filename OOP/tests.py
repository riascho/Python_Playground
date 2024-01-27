import pytest
from main import Franchise

# test that input is time integer
def test_available_menus():
    assert Franchise.available_menus(12) == None

# test available menus when input is not integer but string

# test that menu times are logical (start time < end time)
