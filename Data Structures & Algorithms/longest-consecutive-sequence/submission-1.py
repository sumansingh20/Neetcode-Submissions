class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for x in s:
            if x - 1 not in s:
                curr = x
                count = 1
                while curr + 1 in s:
                    curr += 1
                    count += 1
                longest = max(longest, count)
        return longest