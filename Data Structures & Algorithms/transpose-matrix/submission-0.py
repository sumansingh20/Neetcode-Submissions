class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            ans.append(row)
        return ans