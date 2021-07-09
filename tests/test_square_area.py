import pytest
from src.Square import Square
from src.Triangle import Triangle


def test_square_name():
    figure = Square(1)

    assert figure.name == "Square"


def test_square_area():
    figure = Square(5)
    area = figure.area
    assert area == 25


def test_square_perimeter():
    figure = Square(10)
    area = figure.perimeter

    assert area == 40


def test_circle_add_area():
    figure_square = Square(5)
    figure_triangle = Triangle(13, 14, 15)
    area = figure_square.add_area(figure_triangle)

    assert area == 109


def test_raise_exception():
    figure_square = Square(5)
    with pytest.raises(ValueError):
        figure_square.add_area(1)
