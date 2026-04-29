class Solution:
    def minEatingSpeed(self, suman, h):
        left = 1
        right = max(suman)
        while left < right:
            mid = (left + right) // 2
            total = 0
            for x in suman:
                total += (x + mid - 1) // mid
            if total <= h:
                right = mid
            else:
                left = mid + 1
        return left