class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        # O (nlogn) Solution:
        nums.sort()

        j = 1

        res = 0
        cur = 0
        while j < len(nums):
            if nums[j] - nums[j-1] == 1:
                cur += 1
                j += 1
            elif nums[j] - nums[j-1] == 0:
                j += 1
            else:
                cur = 0
                j += 1

            if cur > res:
                res = cur

        return res + 1