class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(mystr):
            if mystr == "":
                return True
            if mystr in dp:
                return dp[mystr]

            for word in wordDict:
                if mystr.startswith(word):
                    res = dfs(mystr[len(word):])
                    if res:
                        dp[mystr] = res
                        return dp[mystr]
            
            if mystr not in dp:
                dp[mystr] = False
            return dp[mystr]

        
        return dfs(s)
