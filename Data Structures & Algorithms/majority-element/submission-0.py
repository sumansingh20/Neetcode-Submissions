class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for x in nums:
            if count == 0:
                ans = x
            count += 1 if x == ans else -1
        return ans