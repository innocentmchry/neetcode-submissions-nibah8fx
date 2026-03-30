class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        given_sum = sum(nums)
        total_sum = 0
        for i in range(len(nums) + 1):
            total_sum += i
        
        return total_sum - given_sum