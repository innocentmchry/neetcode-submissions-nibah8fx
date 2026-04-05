class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1, 2, 3, 4
        # 4, 5, 6, 7
        # 7, 8, 9, 1
        # 1, 2, 3, 4
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                topleft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l] 
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topleft
            l += 1
            r -= 1


