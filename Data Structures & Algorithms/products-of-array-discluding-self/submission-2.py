class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        preprod = [1] * size
        postprod = [1] * size
        res = [1] * size

        cur = 1
        for i in range(len(nums)):
            preprod[i] = cur
            cur = cur * nums[i]

        cur = 1
        for i in range(len(nums)-1, -1, -1):
            postprod[i] = cur
            cur = cur * nums[i]

        for i in range(len(nums)):
            res[i] = preprod[i] * postprod[i]

        return res