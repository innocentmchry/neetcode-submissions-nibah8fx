class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(depth):
            if depth == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[depth])
            dfs(depth + 1)
            cur.pop()
            dfs(depth + 1)

        dfs(0)
        return res
