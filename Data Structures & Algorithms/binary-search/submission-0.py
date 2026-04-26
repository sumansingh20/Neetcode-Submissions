class Solution:
    def search(self, nums: list[int], target: int) -> int:
        suman_l = 0
        suman_r = len(nums) - 1

        while suman_l <= suman_r:
            suman_mid = (suman_l + suman_r) // 2

            if nums[suman_mid] == target:
                return suman_mid
            elif nums[suman_mid] < target:
                suman_l = suman_mid + 1
            else:
                suman_r = suman_mid - 1
        return -1