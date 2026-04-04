class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mymax = float('-inf')

        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                mymax = max(mymax, product)

        return mymax