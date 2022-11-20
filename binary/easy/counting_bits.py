class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        for i in range(1, n+1):
            output.append(output[i>>1] + i%2)
        return output
