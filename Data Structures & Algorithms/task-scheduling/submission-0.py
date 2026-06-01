class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        mx = max(count.values())
        freq = 0
        for x in count.values():
            if x == mx:
                freq += 1
        ans = (mx - 1) * (n + 1) + freq
        return max(ans, len(tasks))