class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        col = set()
        d1 = set()
        d2 = set()
        def dfs(row):
            if row == n:
                temp = []
                for r in board:
                    temp.append("".join(r))
                ans.append(temp)
                return
            for c in range(n):
                if c in col or (row - c) in d1 or (row + c) in d2:
                    continue
                board[row][c] = "Q"
                col.add(c)
                d1.add(row - c)
                d2.add(row + c)
                dfs(row + 1)
                board[row][c] = "."
                col.remove(c)
                d1.remove(row - c)
                d2.remove(row + c)
        dfs(0)
        return ans