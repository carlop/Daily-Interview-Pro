import unittest

from dip_001_find_pythagorean_tripets.find_pythagorean_triplets\
    import find_pythagorean_triplets


class FindPythagoreanTripletsTest(unittest.TestCase):
    nums_true_1 = [3, 12, 5, 13]
    nums_true_2 = [3, 1, 4, 5]
    nums_true_3 = [60, 61, 6, 11]
    nums_false_1 = [3, 12, 5, 15]
    nums_false_2 = [4, 1, 5, 14]
    nums_false_3 = [6, 11, 32, 60]

    def test_true_1(self):
        result = find_pythagorean_triplets(self.nums_true_1)
        self.assertEqual(True, result)

    def test_true_2(self):
        result = find_pythagorean_triplets(self.nums_true_2)
        self.assertEqual(True, result)

    def test_true_3(self):
        result = find_pythagorean_triplets(self.nums_true_3)
        self.assertEqual(True, result)

    def test_false_1(self):
        result = find_pythagorean_triplets(self.nums_false_1)
        self.assertEqual(False, result)

    def test_false_2(self):
        result = find_pythagorean_triplets(self.nums_false_2)
        self.assertEqual(False, result)

    def test_false_3(self):
        result = find_pythagorean_triplets(self.nums_false_3)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
