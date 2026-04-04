class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        dp = [-1] * len(s)

        def dfs(i):

            # base can be i == len(s)
            # since if 1 digit is taken i > len(s) - 1 is okay 
            # but if 2 digits are taken i becomes == len(s)
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0

            if dp[i] != -1:
                return dp[i]

            # Every dfs call has its own separate res variable
            res = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i + 2)
            
            dp[i] = res

            return res

        return dfs(0)
