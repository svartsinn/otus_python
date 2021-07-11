from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        self.name = 'Rectangle'
        if height:
            self.area = width * height
            self.perimeter = 2 * width * height
        else:
            self.area = width ** 2
            self.perimeter = 4 * width

