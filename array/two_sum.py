class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[(target - num)] ,idx]
            else:
                nums_dict[num] = idx
            
