class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        return next((l for l in range(1, len(nums) + 1) if any(sum(nums[i:i+l]) >= target for i in range(len(nums) - l + 1))), 0)
