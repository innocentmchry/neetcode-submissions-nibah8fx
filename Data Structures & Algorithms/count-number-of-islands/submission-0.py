class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        island = 0

        def bfs(i, j):
            q = collections.deque()
            q.append((i,j))
            visited.add((i,j))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if ((row + dr) in range(len(grid)) and
                        (col + dc) in range(len(grid[0])) and
                        (row + dr, col + dc) not in visited and
                        grid[(row + dr)][col + dc] == "1"):

                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    island += 1

        return island


            




            




