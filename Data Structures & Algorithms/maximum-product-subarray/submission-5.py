class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # concept of trackin min and max
        # kind of pointers to two variables/three
        res = max(nums) # would work if [0, -1] or something
        curmin, curmax = 1, 1

        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            
            temp = n * curmax
            curmax = max(n * curmax, n * curmin, n)
            curmin = min(temp, n * curmin, n)
            res = max(curmax, res)

        return res