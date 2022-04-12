class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_digits = int(''.join(map(str, digits)))
        int_digits = int_digits+1
        int_digits = list(map(int, str(int_digits)))
        return int_digits
