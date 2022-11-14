class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = b
        while carry!=0:
            xor = a ^ b
            carry = (a & b) << 1
            b = carry
            a = xor
        return xor
