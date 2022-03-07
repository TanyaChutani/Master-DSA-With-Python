import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        end = len(x)
        for i in range (0, math.ceil(end/2)):
            if x[i] != x[(end - i) - 1]:
                return False
        return True
        
