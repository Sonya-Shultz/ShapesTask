from Shapes2D.FigureParser import FigureParser
from Shapes2D.Errors.CustomErrors import *
from Shapes2D.Figures.SimplerFigures.Dot import Dot

import pytest

test_data = ["Square TopRight 1 1 Side 1", "Rectangle TopRight 2 2 BottomLeft 1 1", "Circle Center 1 1 Radius 2"]
fp = FigureParser()


def test_FigureParserGetFeomStr_positive_Square():
    fp.set_from_str(test_data[0])
    assert  fp.res_to_str() == "Square Perimeter 4 Area 1"

def test_FigureParserGetFeomStr_positive_Rectangle():
    fp.set_from_str(test_data[1])
    assert  fp.res_to_str() == "Rectangle Perimeter 4 Area 1"

def test_FigureParserGetFeomStr_positive_Circle():
    fp.set_from_str(test_data[2])
    tmp = 3.14159265359 * 4
    assert  fp.res_to_str() == f"Circle Perimeter {tmp} Area {tmp}"

def test_FigureParserGetFeomStr_positive_Triangle():
    fp.set_from_str("Triangle Point1 0 0 Point2 1 1 Point3 0 1")
    p = 3.414213562373095
    a = 0.49999999999999983
    assert fp.res_to_str() == f"Triangle Perimeter {p} Area {a}"

def test_FigureParserGetFeomStr_positive_Triangle2():
    fp.set_from_str("Triangle Point1 0 0 Point2 2 2 Point3 0 2")
    p = 6.82842712474619
    a = 1.9999999999999993
    assert fp.res_to_str() == f"Triangle Perimeter {p} Area {a}"

def test_FigureParserGetFeomStr_negative_figure():
    with pytest.raises(NoSuchFiguresPatternError):
        fp.set_from_str("Squatttte TopRight 1 1 Side 1")

def test_FigureParserGetFeomStr_negative_missingAttribute():
    with pytest.raises(MissingDataError):
        fp.set_from_str("Square TopRight 1 1")
    with pytest.raises(MissingDataError):
        fp.set_from_str("Square 1 1 Side 1")

def test_FigureParserGetFeomStr_negative_missingAttributeValue():
    with pytest.raises(CantParseCoordinatesError):
        fp.set_from_str("Square TopRight 1 Side 1")

def test_FigureParserGetFeomStr_negative_wrongAttributeValue():
    with pytest.raises(CantParseCoordinatesError):
        fp.set_from_str("Square TopRight 1 1.2 Side 1")

def test_FigureParserGetFeomStr_negative_wrongSingleAttributeValue():
    with pytest.raises(CantParseSingleValueError):
        fp.set_from_str("Circle Center 1 1 Radius 2lff")

def test_FigureParserGetFeomStr_negative_negativeValue():
    with pytest.raises(NegativeValueOfMetrixError):
        fp.set_from_str("Square TopRight 1 1 Side -1")

def test_FigureParserGetFeomStr_negative_WrongDotPositionInRectangle():
    with pytest.raises(WrongDotPositionError):
        fp.set_from_str("Rectangle TopRight -2 -2 BottomLeft 1 1")

def test_DotMoreThan_positive():
    d1 = Dot(2, -2, -2)
    d2 = Dot(2, 0, -4)
    d3 = Dot(2, 0, 0)
    d4 = Dot(2, -4, -4)
    assert all(d1.more_then(d4))
    assert any(d1.more_then(d2))
    assert not all (d1.more_then(d3))

def test_Dot_negative():
    with pytest.raises(MissingDataError):
        d1 = Dot(2, -2)

def test_DotMoreThan_negative():
    with pytest.raises(IncomparableDimensions):
        d1 = Dot(2, -2, 2)
        d2 = Dot(3, 0, -4, 6)
        d1.more_then(d2)

