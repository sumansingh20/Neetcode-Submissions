class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, visit):
            visit.add((r, c))
            d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in d:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < row and
                    0 <= nc < col and
                    (nr, nc) not in visit and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visit)
        for i in range(row):
            dfs(i, 0, pacific)
            dfs(i, col - 1, atlantic)
        for j in range(col):
            dfs(0, j, pacific)
            dfs(row - 1, j, atlantic)
        ans = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])
        return ans