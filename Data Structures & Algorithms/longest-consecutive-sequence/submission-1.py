class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Can I do it in O(n). Yes by using a set. Its actually O(n + n) because n is max. It may look like its O(n^2) but its not
        # because we find max only once. :x
        my_set = set(nums)
        
        # 2, 20, 4, 10, 3, 5

        longest = 0
        for item in my_set:
            if (item - 1) in my_set:
                continue
            length = 1
            
            while item + length in my_set:
                length += 1
            
            longest = max(length, longest)

        return longest
            