class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create pre_map or graph

        pre_map = {}
        for i in range(numCourses):
            pre_map[i] = []

        for course, pre in prerequisites:
            pre_map[course].append(pre)

        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            
            if pre_map[cur] == []:
                return True

            visited.add(cur)
            for pre in pre_map[cur]:
                if not dfs(pre): return False # mwnse neibor ni takai loop mwnbanw thangfin

            visited.remove(cur)
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True

        