from unittest import TestCase

import math

from citlab_python_util.geometry.util import get_dist_fast, get_in_dist, get_off_dist

from citlab_python_util.geometry.rectangle import Rectangle


class TestUtil(TestCase):
    def test_check_intersection(self):
        pass

    def test_ortho_connect(self):
        pass

    def test_dist_fast(self):
        bb = Rectangle(0, 0, 10, 10)
        p_list = [[x, y] for x in [-1, 5, 11] for y in [-1, 5, 11]]
        dist_list = []
        for p in p_list:
            dist_list += [get_dist_fast(p, bb)]
        self.assertEqual(2, dist_list[0])
        self.assertEqual(1, dist_list[1])
        self.assertEqual(2, dist_list[2])
        self.assertEqual(1, dist_list[3])
        self.assertEqual(0, dist_list[4])
        self.assertEqual(1, dist_list[5])
        self.assertEqual(2, dist_list[6])
        self.assertEqual(1, dist_list[7])
        self.assertEqual(2, dist_list[8])

    def test_get_in_dist(self):
        points1 = [[1, 1], [0, 0]]
        points2 = [[2, 0], [0, 0]]
        or_vec1 = [1, 0]
        or_vec2 = [1 / math.sqrt(2), 1 / math.sqrt(2)]
        in_dist1 = get_in_dist(points1[0], points1[1], or_vec1[0], or_vec1[1])
        in_dist2 = get_in_dist(points2[0], points2[1], or_vec2[0], or_vec2[1])
        in_dist3 = get_in_dist(points1[1], points1[0], or_vec1[0], or_vec1[1])
        in_dist4 = get_in_dist(points2[1], points2[0], or_vec2[0], or_vec2[1])

        self.assertEqual(1, in_dist1)
        self.assertAlmostEqual(math.sqrt(2), in_dist2, places=8)
        self.assertEqual(-1, in_dist3)
        self.assertAlmostEqual(-math.sqrt(2), in_dist4, places=8)

    def test_get_off_dist(self):
        points1 = [[1, 1], [0, 0]]
        points2 = [[2, 0], [0, 0]]
        or_vec1 = [1, 0]
        or_vec2 = [1 / math.sqrt(2), 1 / math.sqrt(2)]
        in_dist1 = get_off_dist(points1[0], points1[1], or_vec1[0], or_vec1[1])
        in_dist2 = get_off_dist(points2[0], points2[1], or_vec2[0], or_vec2[1])
        in_dist3 = get_off_dist(points1[1], points1[0], or_vec1[0], or_vec1[1])
        in_dist4 = get_off_dist(points2[1], points2[0], or_vec2[0], or_vec2[1])

        self.assertEqual(1, in_dist1)
        self.assertAlmostEqual(math.sqrt(2), in_dist2, places=8)
        self.assertEqual(-1, in_dist3)
        self.assertAlmostEqual(-math.sqrt(2), in_dist4, places=8)

    def test_calc_tols(self):
        pass
