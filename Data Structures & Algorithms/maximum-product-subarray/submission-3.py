class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mymax = float('-inf')
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                mymax = max(prod, mymax)
            
        return mymax