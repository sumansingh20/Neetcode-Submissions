class Solution:
    def rob(self, nums: List[int]):

        if len(nums) == 1:
            return nums[0]

        def solve(arr):

            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):

                take = arr[i] + dp[i - 2]
                skip = dp[i - 1]

                if take > skip:
                    dp[i] = take
                else:
                    dp[i] = skip

            return dp[-1]

        a = solve(nums[:-1])
        b = solve(nums[1:])

        if a > b:
            return a

        return b