class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // len(matrix[0])
            j = mid % len(matrix[0])
            if target == matrix[i][j]:
                return True

            if target > matrix[i][j]:
                left = mid + 1
            else:
                right = mid - 1

        return False 