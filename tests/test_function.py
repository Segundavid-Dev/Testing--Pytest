import pytest
from source.function import divide_number
import source.function as my_function


#Function Based Tests

def test_add():
    result = my_function.add(number_one=3, number_two=7)
    assert result == 10

def test_divide():
    result = divide_number(number_one=10, number_two=2)
    assert result == 5


def test_divide():
    with pytest.raises(ZeroDivisionError): #create a type of exception for ZeroDivisionErrors 🙂
        divide_number(number_one=4, number_two=0)


def test_concanate_strings():
    result = my_function.add(number_one="I like ", number_two="Burger")
    assert result == "I like Burger"