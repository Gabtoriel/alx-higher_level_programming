#!/usr/bin/python3

"""Program to test the base class in the models package."""

import unittest
from models.base import Base


class Test_modelsBase(unittest.TestCase):

    """Testing of the base class of the models package."""

    def test_base_id(self):
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 1)
        self.assertEqual(b4.id, 2)
