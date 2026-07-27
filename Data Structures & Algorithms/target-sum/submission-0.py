class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, s):
            if i == len(nums):
                if s == target:
                    return 1
                return 0

            if (i, s) in dp:
                return dp[(i, s)]

            a = dfs(i + 1, s + nums[i])
            b = dfs(i + 1, s - nums[i])

            dp[(i, s)] = a + b
            return dp[(i, s)]

        return dfs(0, 0)