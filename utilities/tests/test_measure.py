from unittest import TestCase
from citlab_python_util.math import measure


class TestMeasure(TestCase):

    def test_f_measure(self):
        self.assertEqual(0.0, measure.f_measure(0., 0.))
        self.assertEqual(0.0, measure.f_measure(0., 0.5))
        self.assertEqual(0.0, measure.f_measure(0.5, 0.))
        self.assertEqual(0.5, measure.f_measure(0.5, 0.5))
        self.assertAlmostEqual(0.3111, measure.f_measure(0.2, 0.7), 4)
