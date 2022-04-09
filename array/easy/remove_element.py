class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        final_length = 0
        for i in nums:
            if i != val:
                nums[final_length] = i
                final_length += 1
        return final_length
