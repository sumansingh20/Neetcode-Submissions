class Solution:
    def findMin(self, suman):
        l, r = 0, len(suman) - 1
        while l < r:
            mid = (l + r) // 2
            if suman[mid] > suman[r]:
                l = mid + 1
            else:
                r = mid
        return suman[l]