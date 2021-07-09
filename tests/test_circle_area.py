import pytest
from src.Square import Square
from src.Circle import Circle


def test_circle_name():
    figure = Circle(1)

    assert figure.name == "Circle"


def test_circle_area():
    figure = Circle(10)
    area = figure.area
    assert round(area, 2) == 31.42


def test_circle_perimeter():
    figure = Circle(6)
    perimeter = figure.perimeter
    assert round(perimeter, 2) == 37.7


def test_circle_add_area():
    figure_circle = Circle(5)
    figure_square = Square(4)
    area = figure_circle.add_area(figure_square)
    assert round(area, 2) == 31.71


def test_raise_exception():
    figure_circle = Circle(5)
    with pytest.raises(ValueError):
        figure_circle.add_area(1)
