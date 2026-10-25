class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for x in set(nums):
            if nums.count(x) % 2 != 0:
                return False
        return True