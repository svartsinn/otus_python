from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a_side, b_side, c_side):
        self.name = 'Triangle'
        self.perimeter = a_side + b_side + c_side
        self._half_perimeter = (a_side + b_side + c_side) / 2
        self.area = math.sqrt(self._half_perimeter * (self._half_perimeter - a_side) * (self._half_perimeter - b_side)
                              * (self._half_perimeter - c_side))

    def __new__(cls, a_side, b_side, c_side):
        if a_side + b_side > c_side and a_side + c_side > b_side and b_side + c_side > a_side:
            return super(Triangle, cls).__new__(cls)
        else:
            return None
