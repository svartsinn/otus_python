from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        self.name = 'Rectangle'
        self.area = width * height
        self.perimeter = 2 * width * height
