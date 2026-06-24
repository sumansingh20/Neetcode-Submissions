class Solution:
    def orangesRotting(self, grid: List[List[int]]):

        rows = len(grid)
        cols = len(grid[0])

        queue = []
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        minute = 0
        index = 0
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while index < len(queue) and fresh > 0:

            size = len(queue) - index

            for k in range(size):

                row, col = queue[index]
                index += 1

                for dr, dc in direction:

                    nr = row + dr
                    nc = col + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append([nr, nc])

            minute += 1

        if fresh == 0:
            return minute

        return -1