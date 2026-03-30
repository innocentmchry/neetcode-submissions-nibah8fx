class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # most brute for way to solve it

        size = len(nums)
        for i in range(size):
            cur_1 = nums[i]
            for j in range(i+1, size):
                cur_2 = nums[j]
                if cur_1 == cur_2:
                    return True

        return False