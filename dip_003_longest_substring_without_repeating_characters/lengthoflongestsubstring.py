class LengthOfLongestSubstring:
    @staticmethod
    def length_of_longest_substring(s):
        substring_max_length = 0
        substring_length = 0
        char_appearance = {}

        # Iterates the string
        # Saves appearance of each letter in a hashtable/dict
        # If it exists reset substring_length
        for char in s:
            if char in char_appearance:
                substring_length = 0
                char_appearance.clear()
            else:
                substring_length += 1
                if substring_length > substring_max_length:
                    substring_max_length = substring_length
                char_appearance[char] = 1

        return substring_max_length
