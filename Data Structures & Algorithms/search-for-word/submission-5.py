class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if (i not in range(rows) or j not in range(cols)
                or board[i][j] != word[idx] or (i, j) in visited):
                return False
            
            visited.add((i, j))
            for r, c in directions:
                nr, nc = i + r, j + c
                if dfs(nr, nc, idx + 1):
                    return True
            visited.remove((i , j))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False