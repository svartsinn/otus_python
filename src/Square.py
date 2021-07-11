from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(width=size, height=None)
        self.name = 'Square'
