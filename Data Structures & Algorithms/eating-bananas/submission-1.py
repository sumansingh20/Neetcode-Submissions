class Solution:
    def minEatingSpeed(self, suman, h):
        l, r = 1, max(suman)
        while l < r:
            mid = (l + r) // 2
            time = 0
            for x in suman:
                time += (x + mid - 1) // mid
            if time <= h:
                r = mid
            else:
                l = mid + 1
        return l