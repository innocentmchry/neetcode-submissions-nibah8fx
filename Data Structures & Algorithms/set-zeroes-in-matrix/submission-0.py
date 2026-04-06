class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Brute force way to solve it?
        rows, cols = len(matrix), len(matrix[0])

        def makezeros(a, b):
            # make row zero
            for i in range(cols):
                matrix[a][i] = 0

            # make col zero
            for i in range(rows):
                matrix[i][b] = 0

        myset = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    myset.add((i,j))

        for i in range(rows):
            for j in range(cols):
                if (i, j) in myset:
                    makezeros(i, j)
