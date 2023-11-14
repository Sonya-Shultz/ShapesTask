from Shapes2D.Errors.CustomErrors import MissingDataError, IncomparableDimensions

class Dot:
    """
        Class of Dot object.
        Contains its dimension and array of coordinates.

        Var:
        - dimension (int): number of dimention for point.
        - coord (array of int): coordinates for point in choosen dimansion.
    """
    def __init__(self, dimension, *coord):
        self.dimension = dimension
        if self.dimension != len(coord):
            raise MissingDataError("Dot")
        self.coord = []
        for el in coord:
            self.coord.append(el)

    def distance_to(self, dot):
        """
            Calculates diatance between two self and given dot.

            var:
            - dot (Dot obj): another point with same dimension size.

            return:
            - float: Euclidean distance between two dots.
        """
        if self.dimension != dot.dimension:
            raise IncomparableDimensions(self.dimension, dot.dimension, "calculate distance")
        sum_t = 0
        for i in range(self.dimension):
            sum_t += (self.coord[i] - dot.coord[i])**2
        return sum_t**0.5

    def more_then(self, dot):
        """
            Coordinates increasing from top left to bottom right.
            Result - array of dimension size with comparation (>) to oher dot.

            var:
            - dot (Dot obj): another point with same dimension size/

            return:
            - array of bool: pairwise comparison of coordinates
        """
        if self.dimension != dot.dimension:
            raise IncomparableDimensions(self.dimension, dot.dimension, "comparison")
        more_arr = []
        for i in range(self.dimension):
           more_arr.append(self.coord[i] > dot.coord[i])
        return more_arr
