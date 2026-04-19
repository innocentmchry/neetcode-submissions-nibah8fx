class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        grids = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cur = board[i][j]
                    if cur in rows[i] or cur in cols[j] or cur in grids[(i // 3, j // 3)]:
                        return False

                    rows[i].append(cur)
                    cols[j].append(cur)
                    grids[(i // 3, j // 3)].append(cur)

        return True
                    