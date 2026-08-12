class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for arr in intervals:
            if not ans or ans[-1][1] < arr[0]:
                ans.append(arr)
            else:
                ans[-1][1] = max(ans[-1][1], arr[1])
        return ans