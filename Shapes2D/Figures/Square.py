from Shapes2D.Errors.CustomErrors import *
from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.SimplerFigures.Dot import Dot


class Square(Figure):
    """
        Class of Square object.
        Contains its name, side lenght and position of top right corner.

        Const:
        - CORNER_STR (string): keyword for top right corner in input
        - SIDE_STR (string): keyword for side lenght in input

        Var:
        - side (int): length of square side.
        - top_right_dot (Dot obj): Point on n-dimentioonal space (for now 2d) with coordinats of top right corner.
    """

    CORNER_STR = "TopRight"
    SIDE_STR = "Side"
    NAME = "Square"
    side = 0
    top_right_dot = None

    def __init__(self, data):
        super().__init__(data)

    def parse_str(self, data):
        """
            Splits user input by " " (space) and removes figure name.
            Looks for required attributes (coordinate of top right corner and size lenght) then tries to parse and set them.

            var:
            - data (string): string with user input with format "Square TopRight X X Side X" where X is integer numbers and side bigger than 0.
        """
        arr = data.split(" ")[1:]
        try:
            corner_ind = arr.index(self.CORNER_STR)
            side_ind = arr.index(self.SIDE_STR)
        except Exception:
            raise MissingDataError(self.NAME)
        try:
            x = int(arr[corner_ind + 1])
            y = int(arr[corner_ind + 2])
            top_right_dot = Dot(2, x, y)
        except Exception:
            raise CantParseCoordinatesError(self.NAME)
        try:
            s = int(arr[side_ind + 1])
            side = s
        except Exception:
            text = None
            if side_ind + 1 < len(arr):
                text = arr[side_ind + 1]
            raise CantParseSingleValueError(self.NAME, self.SIDE_STR, text)
        if side <= 0:
            raise NegativeValueOfMetrixError(self.SIDE_STR, side)
        self.top_right_dot = top_right_dot
        self.side = side

    def area(self):
        """
            Calculate area of square = side*side.

            return:
            - integer: area of square
        """
        return self.side ** 2

    def perimeter(self):
        """
            Calculate v of square = side+side+side+side = 4*side.

            return:
            - integer: perimeter of square
        """
        return 4 * self.side
