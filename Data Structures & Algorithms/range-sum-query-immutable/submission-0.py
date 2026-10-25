class NumArray:
    def __init__(self, nums: List[int]):
        self.a = [0]
        for x in nums:
            self.a.append(self.a[-1] + x)
    def sumRange(self, left: int, right: int) -> int:
        return self.a[right + 1] - self.a[left]