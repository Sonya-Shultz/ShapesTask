from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.SimplerFigures.Dot import Dot
from Shapes2D.Errors.CustomErrors import *


class Circle(Figure):
    CENTER_STR = "Center"
    RADIUS_STR = "Radius"
    name = "Circle"
    Pi = 3.14159265359
    radius = 0
    center_dot = None

    def __init__(self, data):
        super().__init__(data)

    def parse_str(self, data):
        arr = data.split(" ")[1:]
        try:
            center_ind = arr.index(self.CENTER_STR)
            radius_ind = arr.index(self.RADIUS_STR)
        except Exception:
            raise MissingDataError(self.name)
        try:
            x = int(arr[center_ind + 1])
            y = int(arr[center_ind + 2])
            center_dot = Dot(2, x, y)
        except Exception as e:
            raise CantParseCoordinatesError(self.name)
        try:
            s = int(arr[radius_ind + 1])
            radius = s
        except Exception as e:
            text = None
            if radius_ind + 1 < len(arr):
                text = arr[radius_ind + 1]
            raise CantParseSingleValueError(self.name, self.RADIUS_STR, text)
        if radius <= 0:
            raise NegativeValueOfMetrixError(self.RADIUS_STR, radius)
        self.center_dot = center_dot
        self.radius = radius

    def area(self):
        return self.Pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.Pi * self.radius
