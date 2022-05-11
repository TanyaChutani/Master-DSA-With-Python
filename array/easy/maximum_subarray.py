class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_subarray = 0
        max_subarray = nums[0]

        for i in nums:
            sum_subarray += i
            if sum_subarray > max_subarray:
                max_subarray = sum_subarray
            if sum_subarray < 0:
                sum_subarray = 0
        return max_subarray
