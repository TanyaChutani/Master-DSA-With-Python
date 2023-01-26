class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s.rstrip().split(' ')[-1])
        return length
