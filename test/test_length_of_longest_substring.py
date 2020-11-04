import unittest

from dip_003_longest_substring_without_repeating_characters.\
    lengthoflongestsubstring import \
    LengthOfLongestSubstring


class LengthOfLongestSubstringTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(10, LengthOfLongestSubstring.
                         length_of_longest_substring('abrkaabcdefghijjxxx'))


if __name__ == '__main__':
    unittest.main()
