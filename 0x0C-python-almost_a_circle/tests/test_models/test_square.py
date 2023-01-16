""" Test Module for square.py """
import unittest

Square = __import__("models.square").square.Square


class TestRectangle(unittest.TestCase):
    """ Test class for base.py """

    def test_id(self):
        self.assertEqual(Square(4, id=1).id, 1)

    def test_raiseError(self):
        rect = Square(10, 12, id=1)
        with self.assertRaises(TypeError):
            rect.width = "Lol"
        with self.assertRaises(TypeError):
            rect.height = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            rect.x = {1, 2, 3, 4}
        with self.assertRaises(TypeError):
            rect.y = complex(10, 2.4)
        with self.assertRaises(ValueError):
            rect.width = -10
        with self.assertRaises(ValueError):
            rect.height = -19
        with self.assertRaises(ValueError):
            rect.x = -4
        with self.assertRaises(ValueError):
            rect.y = -4

    def test_area(self):
        rect = Square(3)
        self.assertEqual(rect.area(), 9)
        with self.assertRaises(TypeError):
            rect.area(1)

    def test_str(self):
        rect = Square(4, 2, 1, 12)
        self.assertEqual(str(rect), "[Square] (12) 2/1 - 4")
