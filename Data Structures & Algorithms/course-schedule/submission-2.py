class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection
        adjacency = defaultdict(list)

        for i in range(len(prerequisites)):
            n1, n2 = prerequisites[i]
            adjacency[n1].append(n2)

        visited = set()
        cycle = set()

        def dfs(i):
            if i in visited:
                return False

            if i in cycle:
                return True

            # visited.add(i)
            cycle.add(i)
            for nei in adjacency[i]:
                if dfs(nei):
                    return True
            
            cycle.remove(i)
            return False

        for i in range(numCourses):
            # if i not in visited:
            #     if dfs(i):
            #         return False
            if dfs(i):
                return False

        return True