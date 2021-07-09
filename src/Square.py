from src.Figure import Figure


class Square(Figure):
    def __init__(self, size):
        self.name = 'Square'
        self.area = size ** 2
        self.perimeter = 4 * size
