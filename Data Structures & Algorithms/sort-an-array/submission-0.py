class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def heapify(size, i):
            while True:
                big = i
                l = 2 * i + 1
                r = 2 * i + 2
                if l < size and nums[l] > nums[big]:
                    big = l
                if r < size and nums[r] > nums[big]:
                    big = r
                if big == i:
                    break
                nums[i], nums[big] = nums[big], nums[i]
                i = big
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)
        return nums