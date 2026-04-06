class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # First identify that putting zeros in the same place you already put is repeatition and is a subproblem
        # You can solve it using an array of size m + n. m tracks rows to zero, n tracks zols to zero
        # But there is a better solution which uses just O(1) space

        #x x x x # 1 2 0
        #  x 0 1 # 1 0 2
        #  x 1 1 # 2 1 1
        
        topleft = False
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        topleft = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(1, rows):
                matrix[i][0] = 0

        if topleft:
            for i in range(cols):
                matrix[0][i] = 0

            