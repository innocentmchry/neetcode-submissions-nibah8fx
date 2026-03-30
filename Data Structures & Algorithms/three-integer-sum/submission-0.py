class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_hashset = set()

        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                for k in range(j+1, size):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ls = tuple(sorted([nums[i], nums[j], nums[k]]))
                        my_hashset.add(ls)

        return list(my_hashset)