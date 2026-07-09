class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            if dp[i - 1] < dp[i - 2]:
                dp[i] = cost[i] + dp[i - 1]
            else:
                dp[i] = cost[i] + dp[i - 2]
        if dp[n - 1] < dp[n - 2]:
            return dp[n - 1]
        return dp[n - 2]