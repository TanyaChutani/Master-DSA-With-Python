class Solution:
    def countBits(self, n: int) -> List[int]:
        final_list = []
        for i in range(n+1):
            if i == 0:
                final_list.append(0)
            elif i%2 == 0:
                final_list.append(final_list[i//2])
            else:
                final_list.append(final_list[i//2] + 1)
        return final_list
            
