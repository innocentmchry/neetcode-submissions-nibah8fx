class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) solution without division operation
        prefix = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res