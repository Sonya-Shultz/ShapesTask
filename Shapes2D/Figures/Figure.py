from Shapes2D.Errors.CustomErrors import NoSuchFiguresPatternError


class Figure:
    """
        Main class of shapes.
        Contains its name.

        Const:
        - NAME (string): Name of the shape.
    """
    NAME = "Figure"

    def __init__(self, data):
        self.parse_str(data)

    def parse_str(self, data):
        raise NoSuchFiguresPatternError(data)

    def area(self):
        return 0

    def perimeter(self):
        return 0
