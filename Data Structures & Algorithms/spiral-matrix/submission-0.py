class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #   L       R 
        #   1 2 3 4 4
        # T 3 4 5 4 4
        # B 1 3 4 5 6

        # You should understand the dynamics of traversing in matrices

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        res = []

        while left <= right and top <= bottom:
            # Go from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # Go from topright to bottomright
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if not (left <= right and top <= bottom):
                break

            # Go from right to left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # GO from bottomleft to topleft
            for i in range(bottom, top -1, -1):
                res.append(matrix[i][left])
            left += 1

        return res




