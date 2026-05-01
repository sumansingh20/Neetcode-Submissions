class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        suman = nums1 + nums2
        suman.sort()
        
        n = len(suman)
        
        if n % 2 == 1:
            return float(suman[n // 2])
        else:
            return (suman[n // 2 - 1] + suman[n // 2]) / 2