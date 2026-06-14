class Solution:
    def findWords(self, board, words):
        trie = {}

        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word

        n = len(board)
        m = len(board[0])
        ans = []

        def dfs(i, j, node):
            ch = board[i][j]

            if ch not in node:
                return

            nxt = node[ch]

            if "#" in nxt:
                ans.append(nxt["#"])
                del nxt["#"]

            board[i][j] = "*"

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni = i + dx
                nj = j + dy

                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != "*":
                    dfs(ni, nj, nxt)

            board[i][j] = ch

        for i in range(n):
            for j in range(m):
                dfs(i, j, trie)
        return ans