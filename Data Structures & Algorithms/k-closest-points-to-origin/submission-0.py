class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for x, y in points:
            dist = x * x + y * y
            ans.append([dist, [x, y]])
        ans.sort()
        result = []
        for i in range(k):
            result.append(ans[i][1])
        return result