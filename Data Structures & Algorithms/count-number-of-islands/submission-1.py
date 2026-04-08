class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        self.count = 0
        q = collections.deque()
        def bfs():
            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i,j))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for row, col in directions:
                    c_row = i + row
                    c_col = j + col
                    if (c_row not in range(rows) or c_col not in range(cols)
                        or grid[c_row][c_col] != "1" or (c_row, c_col) in visited):
                        continue
                    q.append((c_row, c_col))
            
            self.count += 1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        q.append((i,j))
                        bfs()               

        return self.count