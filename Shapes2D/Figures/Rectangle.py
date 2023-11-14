from Shapes2D.Errors.CustomErrors import *
from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.SimplerFigures.Dot import Dot


class Rectangle(Figure):
    """
        Class of Rectangle object.
        Contains its name, positions of top right  and bottom left corners, lenghts of wide and height.

        Const:
        - CORNER1_STR (string): keyword for top right corner in input
        - CORNER2_STR (string): keyword for bottom left corner in input

        Var:
        - side1 (int): length of rectangle side.
        - side2 (int): length of rectangle side.
        - top_right_dot (Dot obj): Point on n-dimentioonal space (for now 2d) with coordinats of top right corner.
        - bottom_left_dot (Dot obj): Point on n-dimentioonal space (for now 2d) with coordinats of bottom left corner.
    """
    CORNER1_STR = "TopRight"
    CORNER2_STR = "BottomLeft"
    NAME = "Rectangle"
    top_right_dot = None
    bottom_left_dot = None

    side1 = 0
    side2 = 0

    def __init__(self, data):
        super().__init__(data)

    def parse_str(self, data):
        """
            Splits user input by " " (space) and removes figure name.
            Looks for required attributes (two coordinates of 2d dots) then tries to parse and set them.

            var:
            - data (string): string with user input with format "Rectangle TopRight X X BottomLeft X X" where X is integer numbers.
        """
        arr = data.split(" ")[1:]
        try:
            corner1_ind = arr.index(self.CORNER1_STR)
            corner2_ind = arr.index(self.CORNER2_STR)
        except Exception:
            raise MissingDataError(self.NAME)
        try:
            x = int(arr[corner1_ind + 1])
            y = int(arr[corner1_ind + 2])
            top_right_dot = Dot(2, x, y)
            x = int(arr[corner2_ind + 1])
            y = int(arr[corner2_ind + 2])
            bottom_left_dot = Dot(2, x, y)
        except Exception:
            raise CantParseCoordinatesError(self.NAME)
        more_arr = top_right_dot.more_then(bottom_left_dot)
        if not all(more_arr):
            raise WrongDotPositionError()

        self.top_right_dot = top_right_dot
        self.bottom_left_dot = bottom_left_dot

        self.side1 = self.top_right_dot.coord[0] - self.bottom_left_dot.coord[0]
        self.side2 = self.top_right_dot.coord[1] - self.bottom_left_dot.coord[1]

    def area(self):
        """
            Calculate area of rectangle = side1*side2.

            return:
            - integer: area of rectangle
        """
        return self.side1 * self.side2

    def perimeter(self):
        """
            Calculate perimeter of rectangle = (side1 + side2) * 2.

            return:
            - integer: perimeter of rectangle
        """
        return 2 * self.side1 + 2 * self.side2
