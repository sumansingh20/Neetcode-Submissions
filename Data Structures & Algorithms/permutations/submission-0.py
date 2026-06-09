class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(path, left):
            if len(left) == 0:
                ans.append(path)
                return
            for i in range(len(left)):
                dfs(path + [left[i]], left[:i] + left[i + 1:])
        dfs([], nums)
        return ans