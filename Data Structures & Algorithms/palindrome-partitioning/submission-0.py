class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        def dfs(start):
            if start == n:
                ans.append(path[:])
                return
            for end in range(start, n):
                sub = s[start:end + 1]
                if sub == sub[::-1]:
                    path.append(sub)
                    dfs(end + 1)
                    path.pop()
        dfs(0)
        return ans