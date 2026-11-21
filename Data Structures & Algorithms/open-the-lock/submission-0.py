class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        visited = {"0000"}
        queue = [("0000", 0)]
        idx = 0

        while idx < len(queue):
            state, steps = queue[idx]
            idx += 1

            for i in range(4):
                digit = int(state[i])
                for diff in (-1, 1):
                    nxt_digit = (digit + diff) % 10
                    nxt = state[:i] + str(nxt_digit) + state[i + 1 :]
                    if nxt == target:
                        return steps + 1
                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))

        return -1