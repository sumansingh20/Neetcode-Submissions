class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = [0] * (n + 1)
        
        for t in trust:
            a = t[0]
            b = t[1]
            cnt[a] = cnt[a] - 1
            cnt[b] = cnt[b] + 1
            
        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                return i
                
        return -1