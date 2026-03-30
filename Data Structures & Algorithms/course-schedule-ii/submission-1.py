class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Proper Topo Sort (Kahn's Algorithm)
        # Kahn Algo is a generic way to process a DAG in dependency order

        indegree = [0] * numCourses
        adj_list = []
        for i in range(numCourses):
            adj_list.append([])

        for course, pre in prerequisites:
            indegree[pre] += 1
            adj_list[course].append(pre)

        q = collections.deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        
        while q:
            cur = q.popleft()
            res.append(cur)

            for nei in adj_list[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) == numCourses:
            return res[::-1]
        else:
            return []
