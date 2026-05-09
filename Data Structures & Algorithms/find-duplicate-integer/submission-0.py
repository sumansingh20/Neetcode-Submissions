class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for suman in range(len(nums)-1):
            if nums[suman] == nums[suman+1]:
                return nums[suman]