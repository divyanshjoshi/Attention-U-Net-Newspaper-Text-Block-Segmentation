from unittest import TestCase

import math

from citlab_python_util.geometry import polygon
from citlab_python_util.geometry.polygon import Polygon


class TestPolygon(TestCase):
    def test_get_list_view(self):
        poly_in = Polygon([0, 3, 4, 5, 7, 5], [1, 3, 5, 3, 1, 0], 6)
        res = [(0, 1), (3, 3), (4, 5), (5, 3), (7, 1), (5, 0)]

        self.assertEqual(res, poly_in.as_list())

    def test_translate(self):
        pass

    def test_calculate_bounds(self):
        pass

    def test_update_bounds(self):
        pass

    def test_add_point(self):
        pass

    def test_get_bounding_box(self):
        pass

    def test_blow_up(self):
        poly_in = Polygon([0, 3, 4, 5, 7, 5], [1, 3, 5, 3, 1, 0], 6)
        poly_out = polygon.blow_up(poly_in)
        res = Polygon([0, 1, 2, 3, 4, 4, 5, 5, 6, 7, 6, 5], [1, 2, 2, 3, 4, 5, 4, 3, 2, 1, 1, 0], 12)

        self.assertEqual(res.x_points, poly_out.x_points)
        self.assertEqual(res.y_points, poly_out.y_points)
        self.assertEqual(res.n_points, 12)

    def test_thin_out(self):
        poly_in1 = Polygon([0, 1, 2, 3, 4, 4, 5, 5, 6, 7, 6, 5], [1, 2, 2, 3, 4, 5, 4, 3, 2, 1, 1, 0], 12)
        des_dist_1 = 1  # no changes
        des_dist_2 = 2  # distance of 2
        des_dist_100 = 100  # just consider min points (=20)

        poly1_1 = polygon.thin_out(poly_in1, des_dist_1)
        poly1_2 = polygon.thin_out(poly_in1, des_dist_2)
        poly1_100 = polygon.thin_out(poly_in1, des_dist_100)

        for poly in [poly1_1, poly1_2, poly1_100]:
            self.assertEqual(poly_in1.x_points, poly.x_points)
            self.assertEqual(poly_in1.y_points, poly.y_points)
            self.assertEqual(poly_in1.n_points, poly.n_points)

        poly_in2 = Polygon()
        for (x, y) in zip(range(60), range(60)):
            poly_in2.add_point(x, y)

        poly2_1 = polygon.thin_out(poly_in2, des_dist_1)
        poly2_2 = polygon.thin_out(poly_in2, des_dist_2)
        poly2_100 = polygon.thin_out(poly_in2, des_dist_100)

        self.assertEqual(poly_in2.x_points, poly2_1.x_points)
        self.assertEqual(poly_in2.y_points, poly2_1.y_points)
        self.assertEqual(poly_in2.n_points, poly2_1.n_points)

        self.assertEqual(list(range(0, 58, 2)) + [59], poly2_2.x_points)
        self.assertEqual(list(range(0, 58, 2)) + [59], poly2_2.y_points)
        self.assertEqual(30, poly2_2.n_points)

        self.assertEqual(list(range(0, 30, 3)) + list(range(31, 57, 3)) + [59], poly2_100.x_points)
        self.assertEqual(list(range(0, 30, 3)) + list(range(31, 57, 3)) + [59], poly2_100.y_points)
        self.assertEqual(20, poly2_100.n_points)

    def test_norm_poly_dists(self):
        des_dist = 2
        # Should not be changed (n_points <= 20 after blow_up)
        polygon1 = Polygon(list(range(20)), list(range(20)), 20)
        res1 = polygon1
        # Should be changed, s.t. the normed polygon has 20 (nearly equidistant) pixels
        polygon2 = Polygon(list(range(30)), list(range(30)), 30)
        res2 = Polygon([0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 29],
                       [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 29], 20)
        # Should not be changed, since des_dist = 2
        polygon3 = Polygon(list(range(0, 40, 2)), list(range(0, 40, 2)), 20)
        res3 = polygon3
        # Should be changed, s.t. every two pixels have a distance of des_dist = 2 (except for the last two pixels)
        polygon4 = Polygon(list(range(0, 90, 3)), list(range(0, 90, 3)), 30)
        res4 = Polygon(list(range(0, 86, 2)) + [87], list(range(0, 86, 2)) + [87], 44)

        poly_list = [polygon1, polygon2, polygon3, polygon4]

        normed_poly_list = polygon.norm_poly_dists(poly_list, des_dist)
        res_list = [res1, res2, res3, res4]

        for normed_poly, res in zip(normed_poly_list, res_list):
            self.assertEqual(res.x_points, normed_poly.x_points)
            self.assertEqual(res.y_points, normed_poly.y_points)
            self.assertEqual(res.n_points, normed_poly.n_points)

    def test_calc_reg_line_stats(self):
        # We consider the negative y-values (since we handle computer vision problems..)
        # angle = 0°, n = 0.0
        polygon1 = Polygon(list(range(5)), [0] * 5, 5)
        angle1, n1 = polygon.calc_reg_line_stats(polygon1)

        # angle = 315°, n = 0.0
        polygon2 = Polygon(list(range(5)), list(range(5)), 5)
        angle2, n2 = polygon.calc_reg_line_stats(polygon2)

        # angle = 306°, n = -11/13
        polygon3 = Polygon([0, 1, 2, 2, 3], [1, 2, 3, 4, 5], 5)
        angle3, n3 = polygon.calc_reg_line_stats(polygon3)

        # angle ~ 354°, n = -2,3
        polygon4 = Polygon([0, 1, 2, 2, 3, 4], [1, 2, 3, 4, 5, 0], 6)
        angle4, n4 = polygon.calc_reg_line_stats(polygon4)

        # Example where -math.pi / 2 < angle <= -math.pi / 4 and poly.y_points[0] > poly.y_points[-1]
        polygon5 = Polygon(list(range(100)), list(range(0, 198, 2)) + [-1], 100)
        angle5, n5 = polygon.calc_reg_line_stats(polygon5)

        # Line y = 0 -> n = 0.0 and angle = 0.0
        self.assertEqual(0.0, angle1)
        self.assertEqual(0.0, n1)
        # Line y = -x -> n = 0.0 and angle = -pi/4 + 7*pi/4
        self.assertEqual(7 * math.pi / 4, angle2)
        self.assertEqual(0.0, n2)
        # Line y = -35/26*x - 11/13 -> n = -11/13 and angle = -0.931882342 + 2*pi
        self.assertAlmostEqual(-0.931882342 + 2 * math.pi, angle3, places=8)
        self.assertAlmostEqual(-11 / 13, n3, places=8)
        # Line y = -0.1*x - 2.3 -> n = -2.3 and angle = -0.0996686525 + 2*pi
        self.assertAlmostEqual(-0.0996686525 + 2 * math.pi, angle4, places=8)
        self.assertEqual(-2.3, n4)
        # Line y = -1.8817821782*x - 3.86178217822 -> n = -3.86178217822 and angle = -1.08233671731 + pi
        self.assertAlmostEqual(-1.08233671731 + math.pi, angle5, places=8)
        self.assertAlmostEqual(-3.86178217822, n5, places=8)

    def test_string_to_poly(self):
        poly = polygon.string_to_poly("1,2;2,3;4,5")
        self.assertEqual(poly.n_points, 3)
        self.assertEqual(poly.x_points, [1, 2, 4])
        self.assertEqual(poly.y_points, [2, 3, 5])

    def test_poly_to_string(self):
        poly = Polygon([1, 2, 4], [2, 3, 5], 3)
        res = "1,2;2,3;4,5"
        self.assertEqual(res, polygon.poly_to_string(poly))
