class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            if len(res) == 0:
                res.append([])
                res.append([cur])
            else:
                for j in range(len(res)):
                    res.append(res[j]+[])
                    res.append(res[j]+[cur])
        
        return res[-pow(2, len(nums)):]