class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        if len(edges) == 0:
            return True

        my_graph = {}
        for i in range(n):
            my_graph[i] = []

        for edge in edges:
            l, r = edge
            my_graph[l].append(r)
            my_graph[r].append(l)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            if node in visited:
                return True

            visited.add(node)
            for nei in my_graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node): return False
            
            return True

        status = dfs(edges[0][0], -1)

        if status and len(visited) == n:
            return True
        else:
            return False
        
