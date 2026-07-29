class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            ans = 1
            if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                ans = max(ans, 1 + dfs(i - 1, j))
            if i < m - 1 and matrix[i + 1][j] > matrix[i][j]:
                ans = max(ans, 1 + dfs(i + 1, j))
            if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                ans = max(ans, 1 + dfs(i, j - 1))
            if j < n - 1 and matrix[i][j + 1] > matrix[i][j]:
                ans = max(ans, 1 + dfs(i, j + 1))
            dp[i][j] = ans
            return ans
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res