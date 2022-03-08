class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        output = 0
        for idx in range(0, len(s) - 1):
            if roman_dict[s[idx]] < roman_dict[s[(idx + 1)]]:
                output -= roman_dict[s[idx]]
            else:
                output += roman_dict[s[idx]]
        output += roman_dict[s[len(s) - 1]]
        return output
