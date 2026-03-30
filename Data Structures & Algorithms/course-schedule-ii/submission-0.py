class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []

        for course, pre in prerequisites:
            adj_list[course].append(pre)

        res = []

        # visited checks for cycle
        visited = set()
        # added to check if we already added the node in res
        added = set()
        def dfs(cur):
            if cur in visited:
                return False

            # if adj_list[cur] == []:
            #     return True
            # terminating condition
            if cur in added:
                return True

            # go inside
            visited.add(cur)
            # check all neighbors
            for pre in adj_list[cur]:
                # if cycle detected is reported from dfs call you also return False
                if not dfs(pre): return False
            
            visited.remove(cur) # remove means we backtracked from dfs
            added.add(cur) # add to check if its already added
            res.append(cur)
            # adj_list[cur] = []
            return True

        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return res
            