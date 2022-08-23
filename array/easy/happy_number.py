class Solution:
    def isHappy(self, n: int) -> bool:
        visited_n = []
        while n not in visited_n:
            visited_n.append(n)
            sum_number = 0
            while n:
                sum_number += (n % 10) ** 2
                n //= 10
            n = sum_number
            if n == 1:
                return True
        return False

