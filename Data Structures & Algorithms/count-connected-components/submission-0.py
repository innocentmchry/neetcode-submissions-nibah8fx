class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        my_graph = {i:[] for i in range(n)}

        for l,r in edges:
            my_graph[l].append(r)
            my_graph[r].append(l)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in my_graph[node]:
                dfs(nei)

        count = 0
        for i in range(n):
            prev_value = len(visited)
            dfs(i)
            cur_value = len(visited)
            if cur_value > prev_value:
                count += 1

        return count

