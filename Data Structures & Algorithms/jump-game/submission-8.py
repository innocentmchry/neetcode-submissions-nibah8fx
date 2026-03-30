class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = [False] * len(nums)

        def reachEnd(root):
            if root >= len(nums) - 1:
                return True

            if memo[root]:
                return True
            
            else:
                for i in range(root + 1, root + nums[root] + 1):
                    if reachEnd(i):
                        memo[i] = True
                        return True

            return False

        return reachEnd(0)