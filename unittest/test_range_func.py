import unittest
from range_func import Range

class TestRangeMethods(unittest.TestCase):

    def test_Range(self):
        self.assertRaises(ValueError, Range)
        self.assertRaises(ValueError, Range, 1, 3, 7)

    def test_contains(self):
        self.assertTrue(Range(4).contains(Range(0, 4)))
        self.assertTrue(Range(5).contains(Range(4)))
        self.assertTrue(Range(1, 4).contains(Range(3, 4)))
        self.assertFalse(Range(4).contains(Range(5)))
        self.assertFalse(Range(1, 4).contains(Range(3, 5)))
        self.assertFalse(Range(1, 2).contains(Range(4, 5)))
        self.assertFalse(Range(4, 5).contains(Range(1, 2)))

    def test_overlaps(self):
        self.assertTrue(Range(1, 3).overlaps(Range(2, 3)))
        self.assertTrue(Range(2, 3).overlaps(Range(1, 3)))
        self.assertFalse(Range(1, 5).overlaps(Range(6, 7)))
        self.assertFalse(Range(6, 7).overlaps(Range(1, 5)))

    def test_disjoint(self):
        self.assertTrue(Range(1, 2).disjoint(Range(3, 4)))
        self.assertTrue(Range(3, 4).disjoint(Range(1, 2)))
        self.assertFalse(Range(1, 3).disjoint(Range(2, 3)))
        self.assertFalse(Range(2, 3).disjoint(Range(1, 3)))

    def test_touching(self):
        self.assertTrue(Range(1, 2).touching(Range(2, 7)))
        self.assertTrue(Range(2, 7).touching(Range(1, 2)))
        self.assertFalse(Range(1, 5).touching(Range(4, 7)))
        self.assertFalse(Range(1, 2).touching(Range(4, 7)))
        self.assertFalse(Range(4, 7).touching(Range(1, 2)))

    def test_less_than(self):
        self.assertTrue(Range(1, 3).less_than(Range(3, 10)))
        self.assertTrue(Range(1).less_than(Range(2)))
        self.assertFalse(Range(4, 5).less_than(Range(1, 2)))
        self.assertFalse(Range(2).less_than(Range(1)))
        self.assertFalse(Range(1).less_than(Range(1)))
        self.assertFalse(Range(1, 4).less_than(Range(2, 5)))
        self.assertFalse(Range(2, 6).less_than(Range(1, 4)))

    def test_merge(self):
        self.assertEqual(Range(4).merge(Range(3, 9)), "[0, 9)")
        self.assertEqual(Range(7, 9).merge(Range(8)), "[0, 9)")
        self.assertEqual(Range(3).merge(Range(4, 7)), "[0, 0)")


if __name__ == "__main__":
    unittest.main()