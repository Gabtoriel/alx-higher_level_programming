#!/usr/bin/python3

"""Program to test the rectangle class in the models package."""


import unittest
from models.rectangle import Rectangle

class Testmodel_rect(unittest.TestCase):

    """unittest Class to test the rectangle class in the model package."""

    def test_attr(self):

        """Test to make sure the right attributes are returned."""

        quad = Rectangle(10, 2, 1, 2, 1)
        self.assertEqual(quad.width, 10)
        self.assertEqual(quad.height, 2)
        self.assertEqual(quad.x, 1)
        self.assertEqual(quad.y, 2)
        self.assertEqual(quad.id, 1)
