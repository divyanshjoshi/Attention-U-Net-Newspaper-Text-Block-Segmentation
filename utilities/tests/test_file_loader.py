from unittest import TestCase

from citlab_python_util.io import file_loader


class TestBaselineMeasure(TestCase):
    def test_load_text_file(self):
        filename = ".citlab_python_util/tests/resources/line_reco1.txt"
        res = ["29,80;1321,88", "9,215;506,215;684,199;1139,206",
               "32,329;537,340;621,320;1322,331", "1399,99;2342,98;2611,125",
               "1402,215;2259,206;2599,224", "1395,339;2228,321;2661,342"]

        self.assertEqual(res, file_loader.load_text_file(filename))
