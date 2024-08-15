import pytest
from numb3rs import validate

def test_int_values():
    assert validate("12.12.12.12") == True
    assert validate("275.3.6.28") == False

def test_str_values():
    assert validate("cs50.12.12.12") == False
    assert validate("this.is.cs.50") == False

def test_out_of_range():
    assert validate("12.12.12.12.12") == False
    assert validate("12.12.12") == False
    assert validate("this.is.cs50") == False
