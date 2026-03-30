class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_set = set()
        hash_map = {}

        # this hashmap replaces the previous key, value pair if it sees the same key again.
        # but how does the problem passes all the test cases
        for i, elem in enumerate(nums):
            hash_map[elem] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                compl = 0 - (nums[i] + nums[j])
                if compl in hash_map and hash_map[compl] != i and hash_map[compl] != j:
                    hash_set.add(tuple(sorted([nums[i], nums[j], compl])))

        return list(hash_set)