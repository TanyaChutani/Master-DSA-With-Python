class Solution:
    def addDigits(self, num: int) -> int:
        nums = list(map(int, str(num)))
        if len(nums)>1:
            nums = sum(nums)
            nums = self.addDigits(nums)
        else:
            nums = nums[0]
        return nums
