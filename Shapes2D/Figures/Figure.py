from Shapes2D.Errors.CustomErrors import NoSuchFiguresPatternError


class Figure:
    name = "Figure"

    def __init__(self, data):
        self.parse_str(data)

    def parse_str(self, data):
        raise NoSuchFiguresPatternError(data)

    def area(self):
        return 0

    def perimeter(self):
        return 0
