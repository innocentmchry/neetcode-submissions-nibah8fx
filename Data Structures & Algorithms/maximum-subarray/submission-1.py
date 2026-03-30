class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = -1001
        temp = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                temp = 0
                for k in range(i, j+1):
                    temp += nums[k]                    
                    
                if temp > ms:
                    ms = temp

        return ms