"""Проверка площади и периметра четырёх фигур"""

import unittest

import circle
import rectangle
import square
import triangle


# Площадь круга и длина окружности
# Положительные, нулевые и дробные значения радиуса
class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(circle.area(3), 28.274333882308138, places=7)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_fractional(self):
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483, places=7)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(circle.perimeter(0.5), 3.141592653589793, places=7)


# Площадь и периметр прямоугольника
# Положительные, нулевые и дробные значения сторон
class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(rectangle.area(4, 3), 12)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(4, 0), 0)

    def test_area_fractional(self):
        self.assertAlmostEqual(rectangle.area(2.5, 1.2), 3.0, places=7)

    def test_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(4, 3), 14)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(rectangle.perimeter(2.5, 1.2), 7.4, places=7)


# Площадь и периметр квадрата
# Положительные, нулевые и дробные значения стороны
class SquareTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(square.area(3), 9)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_fractional(self):
        self.assertAlmostEqual(square.area(1.5), 2.25, places=7)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(3), 12)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(square.perimeter(1.5), 6.0, places=7)


# Площадь и периметр треугольника
# Положительные, нулевые и дробные значения сторон и высоты
class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(triangle.area(4, 3), 6.0)

    def test_area_zero(self):
        self.assertEqual(triangle.area(4, 0), 0.0)

    def test_area_fractional(self):
        self.assertAlmostEqual(triangle.area(2.5, 1.2), 1.5, places=7)

    def test_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2, 2.5), 6.0, places=7)
