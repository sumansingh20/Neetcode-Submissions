class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i, j])
        index = 0
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while index < len(queue):
            row, col = queue[index]
            index += 1
            for dr, dc in direction:
                nr = row + dr
                nc = col + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = grid[row][col] + 1
                queue.append([nr, nc])


