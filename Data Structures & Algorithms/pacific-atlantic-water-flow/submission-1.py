class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j, myset, prevheight):
            if (i not in range(rows) or j not in range(cols) or
                (i, j) in myset or heights[i][j] < prevheight):
                return
            
            myset.add((i, j))
        
            for r, c in directions:
                nr, nc = i + r, j + c
                dfs(nr, nc, myset, heights[i][j])

            return

        # top
        for i in range(len(heights[0])):
            dfs(0, i, pacific, float('-inf'))
        
        # left
        for i in range(len(heights)):
            dfs(i, 0, pacific, float('-inf'))

        # bot
        for i in range(len(heights[0])):
            dfs(len(heights)-1, i, atlantic, float('-inf'))
        
        # right
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, atlantic, float('-inf'))

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res