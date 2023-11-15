from Shapes2D.Figures.Figure import Figure
from Shapes2D.Figures.SimplerFigures.Dot import Dot
from Shapes2D.Errors.CustomErrors import *

class Triangle(Figure):
    NAME = "Triangle"
    CORNER1_STR = "Point1"
    CORNER2_STR = "Point2"
    CORNER3_STR = "Point3"

    side1 = 0
    side2 = 0
    side3 = 0
    point1 = None
    point2 = None
    point3 = None

    def parse_str(self, data):
        arr = data.split(" ")[1:]
        try:
            point1_c = arr.index(self.CORNER1_STR)
            point2_c = arr.index(self.CORNER2_STR)
            point3_c = arr.index(self.CORNER3_STR)
        except Exception:
            raise MissingDataError(self.NAME)
        try:
            x = int(arr[point1_c + 1])
            y = int(arr[point1_c + 2])
            point1 = Dot(2, x, y)
            x = int(arr[point2_c + 1])
            y = int(arr[point2_c + 2])
            point2 = Dot(2, x, y)
            x = int(arr[point3_c + 1])
            y = int(arr[point3_c + 2])
            point3 = Dot(2, x, y)
        except Exception:
            raise CantParseCoordinatesError(self.NAME)
        side1 = point1.distance_to(point2)
        side2 = point2.distance_to(point3)
        side3 = point3.distance_to(point1)
        #
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = self.perimeter() / 2.0
        return (p * ( p - self.side1 ) * ( p - self.side2 ) * ( p - self.side3 )) ** 0.5

    def perimeter(self):
        return self.side1+self.side2+self.side3