class CountSquares:
    def __init__(self):
        self.counts = {}
    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]
        self.counts[(x, y)] = self.counts.get((x, y), 0) + 1
    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        ans = 0
        for (a, b), c in self.counts.items():
            if a == x or abs(a - x) != abs(b - y):
                continue
            ans += (
                c
                * self.counts.get((a, y), 0)
                * self.counts.get((x, b), 0)
            )
        return ans