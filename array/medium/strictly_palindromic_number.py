class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            new_n = i ** n
            reverse = 0
            while new_n > 0:
                digit = new_n % 10
                reverse = reverse * 10 + digit
                new_n = new_n // 10
            if i ** n != reverse:
                return False
        return True

