class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR solution. What a brainfuck solution
        # XOR with 0 gives you the same number
        # XOR with 1 gives you the complement

        xor = len(nums)
        for i in range(len(nums)):
            xor ^= i ^ nums[i]
        
        return xor