import pytest
from src.Rectangle import Rectangle
from src.Square import Square


def test_rectangle_name():
    figure = Rectangle(2, 4)

    assert figure.name == "Rectangle"


def test_rectangle_area():
    figure = Rectangle(5, 6)
    area = figure.area

    assert area == 30


def test_rectangle_perimeter():
    figure = Rectangle(7, 8)
    perimeter = figure.perimeter

    assert perimeter == 112


def test_rectangle_add_area():
    figure_triangle = Rectangle(7, 8)
    figure_rectangle = Square(10)
    area = figure_triangle.add_area(figure_rectangle)

    assert round(area, 2) == 156


def test_raise_exception():
    figure_triangle = Rectangle(7, 8)
    with pytest.raises(ValueError):
        figure_triangle.add_area(1)
