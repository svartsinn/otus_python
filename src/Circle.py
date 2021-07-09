from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        self.name = 'Circle'
        self.area = math.pi * radius
        self.perimeter = 2 * math.pi * radius
