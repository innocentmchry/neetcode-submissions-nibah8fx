class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Let me try it in brute force way first
        n = len(matrix)
        mat = []
        for i in range(n):
            mat.append([0] * n)

        for i in range(n):
            for j in range(n):
                mat[i][j] = matrix[n-1-j][i]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = mat[i][j]