import pytest
from calculator import calculation

# test calculation logic
def test_calculation_add():
    result = calculation(5, 3, '+') # we will input 5, 3 and +
    assert result == 8 # 5 + 3 = 8

def test_calculation_subtract():
    result = calculation(5, 3, '-')
    assert result == 2