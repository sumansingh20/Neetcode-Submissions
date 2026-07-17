class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                length = len(word)

                if i + length <= n and s[i:i + length] == word:
                    if dp[i + length]:
                        dp[i] = True
                        break
        return dp[0]