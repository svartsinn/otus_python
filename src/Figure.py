class Figure:
    def __new__(cls, *args, **kwargs):
        if cls is Figure:
            raise TypeError("base class may not be instantiated")
        return object.__new__(cls)

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError
