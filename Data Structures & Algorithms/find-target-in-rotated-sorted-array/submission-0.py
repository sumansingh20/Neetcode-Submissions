class Solution:
    def search(self, suman, target):
        l, r = 0, len(suman)-1
        while l <= r:
            mid = (l+r)//2
            if suman[mid] == target:
                return mid
            if suman[l] <= suman[mid]:
                if suman[l] <= target < suman[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if suman[mid] < target <= suman[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1