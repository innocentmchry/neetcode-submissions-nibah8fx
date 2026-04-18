class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mymax = 0
        visited = set()

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            count = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                curx, cury = q.popleft()
                count += 1
                # visited.add((curx, cury))
                for r, c in directions:
                    nr, nc = r + curx, c + cury
                    if (nr in range(rows) and nc in range(cols)
                        and (nr, nc) not in visited and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return count


        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    res = bfs(i, j)
                    mymax = max(res, mymax)

        return mymax