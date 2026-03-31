class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci Solution
        one = 1
        two = 1
        for i in range(n-1):
            temp = two
            two = temp + one
            one = temp

        return two