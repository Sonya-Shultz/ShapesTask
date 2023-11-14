from Shapes2D.Errors.CustomErrors import *
from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.SimplerFigures.Dot import Dot


class Rectangle(Figure):
    CORNER1_STR = "TopRight"
    CORNER2_STR = "BottomLeft"
    name = "Rectangle"
    top_right_dot = None
    bottom_left_dot = None

    side1 = 0
    side2 = 0

    def __init__(self, data):
        super().__init__(data)

    def parse_str(self, data):
        arr = data.split(" ")[1:]
        try:
            corner1_ind = arr.index(self.CORNER1_STR)
            corner2_ind = arr.index(self.CORNER2_STR)
        except Exception:
            raise MissingDataError(self.name)
        try:
            x = int(arr[corner1_ind + 1])
            y = int(arr[corner1_ind + 2])
            top_right_dot = Dot(2, x, y)
            x = int(arr[corner2_ind + 1])
            y = int(arr[corner2_ind + 2])
            bottom_left_dot = Dot(2, x, y)
        except Exception:
            raise CantParseCoordinatesError(self.name)
        more_arr = top_right_dot.more_then(bottom_left_dot)
        if not all(more_arr):
            raise WrongDotPositionError()

        self.top_right_dot = top_right_dot
        self.bottom_left_dot = bottom_left_dot

        self.side1 = self.top_right_dot.coord[0] - self.bottom_left_dot.coord[0]
        self.side2 = self.top_right_dot.coord[1] - self.bottom_left_dot.coord[1]

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * self.side1 + 2 * self.side2
