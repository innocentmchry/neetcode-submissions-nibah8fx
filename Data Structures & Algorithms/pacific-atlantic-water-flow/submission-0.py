class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        num_rows, num_cols = len(heights), len(heights[0])
        res = []

        def dfs(r, c, my_set, prevheight):
            if r >= num_rows or c >= num_cols or r < 0 or c < 0 or ((r,c) in my_set) or (heights[r][c] < prevheight):
                return
            
            my_set.add((r,c))
            dfs(r-1, c, my_set, heights[r][c])
            dfs(r+1, c, my_set, heights[r][c])
            dfs(r, c-1, my_set, heights[r][c])
            dfs(r, c+1, my_set, heights[r][c])

        for r in range(num_rows):
            dfs(r, 0, pacific, float('-inf'))
            dfs(r, num_cols-1, atlantic, float('-inf'))

        for c in range(num_cols):
            dfs(0, c, pacific, float('-inf'))
            dfs(num_rows-1, c, atlantic, float('-inf'))

        for r in range(num_rows):
            for c in range(num_cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r, c])

        return res





