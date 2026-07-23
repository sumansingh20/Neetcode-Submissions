class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = {}

        def dfs(i, buy):
            if i >= n:
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]

            if buy:
                a = dfs(i + 1, 1)
                b = dfs(i + 1, 0) - prices[i]
                dp[(i, buy)] = max(a, b)
            else:
                a = dfs(i + 1, 0)
                b = dfs(i + 2, 1) + prices[i]
                dp[(i, buy)] = max(a, b)

            return dp[(i, buy)]

        return dfs(0, 1)