class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every row
        # check every column
        # check every grid
        # O (3*9*9) = O(1) Solution, O(1) Space
        # checking every row

        for i in range(9):
            myset = set()
            for j in range(9):
                cur = board[i][j]
                if cur != ".":
                    if cur in myset:
                        return False
                    else:
                        myset.add(cur)
                
        # check every column

        for i in range(9):
            myset = set()
            for j in range(9):
                cur = board[j][i]
                if cur != ".":
                    if cur in myset:
                        return False
                    else:
                        myset.add(cur)

        # check every grid

        for row_grid in [0, 3, 6]:
            for col_grid in [0, 3, 6]:
                myset = set()
                for i in range(3):
                    for j in range(3):
                        cur = board[row_grid + i][col_grid + j]
                        if cur != ".":
                            if cur in myset:
                                return False
                            else:
                                myset.add(cur)

        return True
        
                
