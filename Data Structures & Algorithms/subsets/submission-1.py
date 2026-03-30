# Better solution according to chad gpt
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            cur = []
            for elem in res:
                cur.append(elem + [num])
            
            res.extend(cur)
        
        return res
