class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Only one loop instead of 2 for computing sum. simple math

        res = len(nums)
        for i in range(len(nums)):
            res = res + i - nums[i]

        return res