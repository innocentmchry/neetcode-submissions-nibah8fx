class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myset = set()
        for n in nums:
            myset.add(n)
        
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] - 1 in myset:
                continue

            length = 1
            while nums[i] + length in myset:
                length += 1
            
            maxcount = max(length, maxcount)

        return maxcount
                