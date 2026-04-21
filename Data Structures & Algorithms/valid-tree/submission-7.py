class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
        
        adj = defaultdict(list)
        for i in range(len(edges)):
            l, r = edges[i]
            adj[l].append(r)
            adj[r].append(l)


        visited = set()
        cycle = set()
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            

            return True

        status = dfs(edges[0][0], -1)
        if status and len(visited) == n:
            return True
        
        return False