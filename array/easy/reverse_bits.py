class Solution:
    def reverseBits(self, n: int) -> int:
        final_output = 0
        for _ in range(0,32):
            final_output <<= 1
            final_output = final_output | (n & 1)
            n >>= 1
        return final_output
