class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [1,2,3] len = 3
        my_set = set()

        for i in range(len(nums)):
            my_set.add(nums[i])

        for i in range(len(nums) + 1):
            if i not in my_set:
                return i