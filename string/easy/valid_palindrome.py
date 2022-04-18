import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ("".join(re.findall("[a-zA-Z0-9]+", s))).lower()
        length_sentence = len(sentence)
        if length_sentence == 0: return True
        if length_sentence == 1: return True
        for i in range(length_sentence//2):
            if sentence[i] == sentence[length_sentence-i-1]:
                pass
            else:
                return False
        return True
