from unittest import TestCase
from citlab_python_util.math import rounding


class TestRounding(TestCase):

    def test_round_to_nearest_integer(self):
        self.assertEqual(1, rounding.round_to_nearest_integer(1))
        self.assertEqual(2, rounding.round_to_nearest_integer(1.5))
        self.assertEqual(3, rounding.round_to_nearest_integer(2.5))
