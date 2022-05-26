class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = 0
        
        for i in nums:
            if i != 0:
                nums[non_zero] = i
                non_zero += 1
        for i in range(non_zero, len(nums)):
            nums[i] = 0
            
