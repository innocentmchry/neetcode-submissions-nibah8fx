class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # I complicated too much in the solution
        # Just keep it simple
        myset = set()
        mymap = {}
        for i, num in enumerate(nums):
            mymap[num] = i

        # 0, 1, 2, 3 = 4 - 2 = 1
        # 1, 1, 0, 2
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in mymap and mymap[complement] != i and mymap[complement] != j:
                    myset.add(tuple(sorted([nums[i], nums[j], complement])))
        
        return list(myset)