class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {i: nums.count(i) for i in set(nums)}
        final_output = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)[0][0]
        return final_output
