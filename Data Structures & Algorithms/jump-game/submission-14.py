class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # I want attempt the O(n) solution now
        r = len(nums) - 1
        step = 0
        for i in range(len(nums) - 2, -1, -1):
            step += 1
            cur = nums[i]
            if cur >= step:
                r = i
                step = 0

        if r == 0:
            return True
        else:
            return False