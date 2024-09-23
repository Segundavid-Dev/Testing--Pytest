import pytest
import source.shapes as shapes


@pytest.fixture  #python Fixtures
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)



def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)
