class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # bit manipulation
        total = len(nums)
        res = []
        for i in range(1 << total):
            cur = []
            for j in range(total):
                if (i & (1 << j)):
                    cur.append(nums[j])
            
            res.append(cur)
        
        return res