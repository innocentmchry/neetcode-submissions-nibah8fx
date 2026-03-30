class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(nums)):
            my_map[nums[i]] = i

        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in my_map and i != my_map[compl]:
                return [i, my_map[compl]] if i <= my_map[compl] else [my_map[compl], i]