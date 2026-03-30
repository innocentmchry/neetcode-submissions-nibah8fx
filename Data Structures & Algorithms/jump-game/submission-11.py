class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = [None] * len(nums)

        def reachEnd(root):
            if root >= len(nums) - 1:
                return True

            if memo[root] is not None:
                return memo[root]

            for i in range(root + 1, root + nums[root] + 1):
                if reachEnd(i):
                    memo[i] = True
                    return True

            memo[root] = False
            return False

        return reachEnd(0)