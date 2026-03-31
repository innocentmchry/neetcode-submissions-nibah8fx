class Solution:
    def climbStairs(self, n: int) -> int:

        my_dp = [-1] * n
        
        def dfs(step):
            if step > n:
                return 0
            if step == n:
                return 1

            if my_dp[step] != -1:
                return my_dp[step]

            my_dp[step] = dfs(step+1) + dfs(step+2)
            return my_dp[step]
            

        return dfs(0)