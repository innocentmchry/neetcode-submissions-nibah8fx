class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Very efficient Solution
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur != ".":
                    if (cur in rows[r] or cur in cols[c]
                        or cur in grid[(r // 3, c // 3)]):
                        return False
                    
                    rows[r].add(cur)
                    cols[c].add(cur)
                    grid[(r // 3, c // 3)].add(cur)

        return True

        
                
