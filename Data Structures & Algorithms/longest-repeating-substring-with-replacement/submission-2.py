class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force solution
        res = 0

        for i in range(len(s)):
            mymap = {}
            curmax = 0
            for j in range(i, len(s)):
                mymap[s[j]] = 1 + mymap.get(s[j], 0)
                curmax = max(curmax, mymap[s[j]])

                if j - i + 1 <= curmax + k:
                    res = max(j - i + 1, res)

        return res