class Solution:
    def maxProduct(self, nums: List[int]):
        mx = nums[0]
        mn = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            a = nums[i]
            b = mx * nums[i]
            c = mn * nums[i]
            mx = max(a, b, c)
            mn = min(a, b, c)
            if mx > ans:
                ans = mx
        return ans