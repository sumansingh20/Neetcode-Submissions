class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        best_max = nums[0]
        curr_max = 0
        best_min = nums[0]
        curr_min = 0

        for num in nums:
            total_sum += num
            curr_max = max(num, curr_max + num)
            best_max = max(best_max, curr_max)
            curr_min = min(num, curr_min + num)
            best_min = min(best_min, curr_min)

        if best_max < 0:
            return best_max

        circular_max = total_sum - best_min
        return max(best_max, circular_max)