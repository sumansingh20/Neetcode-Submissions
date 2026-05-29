class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.suman = nums
        heapq.heapify(self.suman)
        while len(self.suman) > k:
            heapq.heappop(self.suman)
    def add(self, val):
        heapq.heappush(self.suman, val)
        if len(self.suman) > self.k:
            heapq.heappop(self.suman)
        return self.suman[0]