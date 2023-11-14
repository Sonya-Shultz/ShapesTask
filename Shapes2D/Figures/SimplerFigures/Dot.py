from Shapes2D.Errors.CustomErrors import MissingDataError, IncomparableDimensions

class Dot:
    def __init__(self, dimension, *coord):
        self.dimension = dimension
        if self.dimension != len(coord):
            raise MissingDataError("Dot")
        self.coord = []
        for el in coord:
            self.coord.append(el)

    def distance_to(self, dot):
        if self.dimension != dot.dimension:
            raise IncomparableDimensions(self.dimension, dot.dimension, "calculate distance")
        sum_t = 0
        for i in range(self.dimension):
            sum_t += (self.coord[i] - dot.coord[i])**2
        return sum_t**0.5

    def more_then(self, dot):
        if self.dimension != dot.dimension:
            raise IncomparableDimensions(self.dimension, dot.dimension, "comparison")
        more_arr = []
        for i in range(self.dimension):
           more_arr.append(self.coord[i] > dot.coord[i])
        return more_arr
