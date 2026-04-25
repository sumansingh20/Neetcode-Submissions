class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        suman_q = deque()
        suman_ans = []
        for i in range(len(nums)):
            while suman_q and suman_q[0] <= i - k:
                suman_q.popleft()
            while suman_q and nums[suman_q[-1]] < nums[i]:
                suman_q.pop()
            suman_q.append(i)
            if i >= k - 1:
                suman_ans.append(nums[suman_q[0]])
        return suman_ans