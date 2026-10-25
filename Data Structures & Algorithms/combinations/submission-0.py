class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curr = []
        
        def solve(start):
            if len(curr) == k:
                ans.append(list(curr))
                return
                
            for i in range(start, n + 1):
                curr.append(i)
                solve(i + 1)
                curr.pop()
                
        solve(1)
        return ans