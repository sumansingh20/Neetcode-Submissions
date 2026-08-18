class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q = sorted((x, i) for i, x in enumerate(queries))

        ans = [-1] * len(queries)
        heap = []
        j = 0

        def push(item):
            heap.append(item)
            i = len(heap) - 1

            while i > 0:
                p = (i - 1) // 2

                if heap[p] <= heap[i]:
                    break

                heap[p], heap[i] = heap[i], heap[p]
                i = p

        def pop():
            heap[0] = heap[-1]
            heap.pop()

            i = 0

            while i < len(heap):
                left = 2 * i + 1
                right = left + 1
                small = i

                if left < len(heap) and heap[left] < heap[small]:
                    small = left

                if right < len(heap) and heap[right] < heap[small]:
                    small = right

                if small == i:
                    break

                heap[i], heap[small] = heap[small], heap[i]
                i = small

        for x, index in q:

            while j < len(intervals) and intervals[j][0] <= x:
                l, r = intervals[j]
                push((r - l + 1, r))
                j += 1

            while heap and heap[0][1] < x:
                pop()

            if heap:
                ans[index] = heap[0][0]

        return ans