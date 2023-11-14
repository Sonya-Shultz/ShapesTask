from Shapes2D.Errors.CustomErrors import *
from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.SimplerFigures.Dot import Dot


class Square(Figure):
    CORNER_STR = "TopRight"
    SIDE_STR = "Side"
    name = "Square"
    side = 0
    top_right_dot = None

    def __init__(self, data):
        super().__init__(data)

    def parse_str(self, data):
        arr = data.split(" ")[1:]
        try:
            corner_ind = arr.index(self.CORNER_STR)
            side_ind = arr.index(self.SIDE_STR)
        except Exception:
            raise MissingDataError(self.name)
        try:
            x = int(arr[corner_ind + 1])
            y = int(arr[corner_ind + 2])
            top_right_dot = Dot(2, x, y)
        except Exception:
            raise CantParseCoordinatesError(self.name)
        try:
            s = int(arr[side_ind + 1])
            side = s
        except Exception:
            text = None
            if side_ind + 1 < len(arr):
                text = arr[side_ind + 1]
            raise CantParseSingleValueError(self.name, self.SIDE_STR, text)
        if side <= 0:
            raise NegativeValueOfMetrixError(self.SIDE_STR, side)
        self.top_right_dot = top_right_dot
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side
