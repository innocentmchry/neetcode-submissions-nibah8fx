class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = -1001
        temp = 0

        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]                                        
                if temp > ms:
                    ms = temp

        return ms