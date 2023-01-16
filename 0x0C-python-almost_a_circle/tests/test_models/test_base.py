""" Test Module for base.py """
import unittest

Base = __import__("models.base").base.Base


class TestRectangle(unittest.TestCase):
    """ Test class for base.py """

    def test_id(self):
        self.assertEqual(Base().id, 1)
