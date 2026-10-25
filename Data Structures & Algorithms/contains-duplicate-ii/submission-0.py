class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        n = len(nums)
        for i in range(n):
            x = nums[i]
            if x in d:
                if i - d[x] <= k:
                    return True
            d[x] = i
        return False