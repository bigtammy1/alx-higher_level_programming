""" Test Module for rectangle.py """
import unittest
Rectangle = __import__("models.rectangle").rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class for rectangle.py """

    def test_id(self):
        rect = Rectangle(10, 12, id=1)
        self.assertEqual(rect.id, 1)

    def test_raiseError(self):
        rect = Rectangle(10, 12, id=1)
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
        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)
        with self.assertRaises(TypeError):
            rect.area(1)

    def test_str(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect), "[Rectangle] (12) 2/1 - 4/6")
