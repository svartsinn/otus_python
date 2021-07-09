import pytest
from src.Rectangle import Rectangle
from src.Triangle import Triangle


def test_triangle_name():
    figure = Triangle(5, 6, 7)

    assert figure.name == "Triangle"


def test_triangle_area():
    figure = Triangle(5, 6, 7)
    area = figure.area

    assert round(area, 2) == 14.7


def test_triangle_perimeter():
    figure = Triangle(7, 8, 9)
    perimeter = figure.perimeter

    assert perimeter == 24


def test_triangle_add_area():
    figure_triangle = Triangle(7, 8, 9)
    figure_rectangle = Rectangle(13, 14)
    area = figure_triangle.add_area(figure_rectangle)

    assert round(area, 2) == 208.83


def test_triangle_with_incorrect_sides():
    figure_triangle = Triangle(3, 2, 1)

    assert figure_triangle is None


def test_raise_exception():
    figure_triangle = Triangle(7, 8, 9)
    with pytest.raises(ValueError):
        figure_triangle.add_area(1)
