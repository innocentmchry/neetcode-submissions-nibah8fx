class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        my_graph = {i:[] for i in range(n)}

        for l,r in edges:
            my_graph[l].append(r)
            my_graph[r].append(l)

        visited = set()

        q = collections.deque()

        def bfs():
            while q:
                cur = q.popleft()
                if cur in visited:
                    continue

                visited.add(cur)
                for nei in my_graph[cur]:
                    q.append(nei)


        count = 0
        for i in range(n):
            prev_value = len(visited)
            q.append(i)
            bfs()
            cur_value = len(visited)
            if cur_value > prev_value:
                count += 1

        return count

