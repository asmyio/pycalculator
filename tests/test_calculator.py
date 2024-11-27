import pytest
from calculator import calculation, saja

def addstuff(x):
    result = x + 1
    return result

# test calculation logic
def test_calculation_add():
    list_of_num = [2,3,4,5,6]
    for x in list_of_num:
        result = calculation(x, 1, '+')
        assert result == addstuff(x)

def test_calculation_subtract():
    result = calculation(5, 3, '-')
    assert result == 2