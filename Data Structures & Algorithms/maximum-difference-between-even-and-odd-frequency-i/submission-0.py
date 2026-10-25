class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for x in s:
            freq[x] = freq.get(x, 0) + 1
        odd = 0
        even = 100
        for x in freq.values():
            if x % 2:
                odd = max(odd, x)
            else:
                even = min(even, x)
        return odd - even