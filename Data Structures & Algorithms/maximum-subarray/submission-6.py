class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        l = 0
        res = nums[l]
        cur = 0
        for i in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            res = max(cur, res)

        return res