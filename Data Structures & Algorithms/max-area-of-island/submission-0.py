class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        max_area = 0

        def bfs(i ,j):
            curr_area = 0
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            curr_area += 1

            # down, up, right, left
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    drow, dcol = row + dr, col + dc
                    if (drow in range(rows) and
                        dcol in range(cols) and
                        grid[drow][dcol] == 1 and
                        (drow, dcol) not in visited):
                        q.append((drow, dcol))
                        visited.add((drow, dcol))
                        curr_area += 1

            return curr_area


        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:        
                    curr_max = bfs(i, j)
                    max_area = max(curr_max, max_area)

        return max_area