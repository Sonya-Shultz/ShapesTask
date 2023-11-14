from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.SimplerFigures.Dot import Dot
from Shapes2D.Errors.CustomErrors import *


class Circle(Figure):
    """
        Class of Circle object.
        Contains its name, positions of center and radius.

        Const:
        - CENTER_STR (string): keyword for center in input
        - RADIUS_STR (string): keyword for radius in input
        - Pi (float): value of Pi up to 11 digits after comma

        Var:
        - radius (int): radius of circle.
        - center_dot (Dot obj): Point on n-dimentioonal space (for now 2d) with coordinats of ceter of the circle.
    """
    CENTER_STR = "Center"
    RADIUS_STR = "Radius"
    NAME = "Circle"
    Pi = 3.14159265359
    radius = 0
    center_dot = None

    def __init__(self, data):
        super().__init__(data)

    def parse_str(self, data):
        """
            Splits user input by " " (space) and removes figure name.
            Looks for required attributes (center coors and radius) then tries to parse and set them.

            var:
            - data (string): string with user input with format "Circle Center X X Radius X" where X is integer numbers and radius bigger then 0.
        """
        arr = data.split(" ")[1:]
        try:
            center_ind = arr.index(self.CENTER_STR)
            radius_ind = arr.index(self.RADIUS_STR)
        except Exception:
            raise MissingDataError(self.NAME)
        try:
            x = int(arr[center_ind + 1])
            y = int(arr[center_ind + 2])
            center_dot = Dot(2, x, y)
        except Exception as e:
            raise CantParseCoordinatesError(self.NAME)
        try:
            s = int(arr[radius_ind + 1])
            radius = s
        except Exception as e:
            text = None
            if radius_ind + 1 < len(arr):
                text = arr[radius_ind + 1]
            raise CantParseSingleValueError(self.NAME, self.RADIUS_STR, text)
        if radius <= 0:
            raise NegativeValueOfMetrixError(self.RADIUS_STR, radius)
        self.center_dot = center_dot
        self.radius = radius

    def area(self):
        """
            Calculate area of circle = PI * r ^ 2.

            return:
            - integer: area of circle
        """
        return self.Pi * (self.radius ** 2)

    def perimeter(self):
        """
            Calculate perimeter of circle = 2 * PI * r.

            return:
            - float: perimeter of circle
        """
        return 2 * self.Pi * self.radius
