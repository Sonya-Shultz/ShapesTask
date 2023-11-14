class NegativeValueOfMetrixError(Exception):
    def __init__(self, metrix_name, metrix_val):
        message = f"Negative value for {metrix_name} ({metrix_val})."
        super().__init__(message)


class CantParseSingleValueError(Exception):
    def __init__(self, fig_name, metrix_name, metrix_val):
        text = "'Data not provided at all!'"
        if metrix_val:
            text = metrix_val
        message = f"Can't parse value of {fig_name} for {metrix_name} (is {text})."
        super().__init__(message)


class CantParseCoordinatesError(Exception):
    def __init__(self, metrix_name):
        message = f"Can't parse coordinates for {metrix_name}"
        super().__init__(message)


class WrongDotPositionError(Exception):
    def __init__(self):
        message = "Wrong dots position."
        super().__init__(message)


class NoSuchFiguresPatternError(Exception):
    def __init__(self, str_data):
        message = f'No figure pattern for this string "{str_data}".'
        super().__init__(message)


class MissingDataError(Exception):
    def __init__(self, fig_name):
        message = f"Not all data provided! Can't build a(n) {fig_name}."
        super().__init__(message)

class IncomparableDimensions(Exception):
    def __init__(self, d1, d2, to_do_text):
        message = f"Attempt of {to_do_text} of dots of two different dimensions ({d1} and {d2})"
        super().__init__(message)