class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return
        for idx, i in enumerate(nums[:-2]):
            if nums[idx] <= nums[idx + 1]:
                idx1 = idx + 1
                for idx_reverse in reversed(range(len(nums))):
                    if nums[idx_reverse] >= nums[idx1]:
                        nums[idx1], nums[idx_reverse] = nums[idx_reverse], nums[idx1]
                nums[idx1:-1].reverse()
