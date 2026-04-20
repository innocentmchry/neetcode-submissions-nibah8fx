class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # optimal solution using sliding window
        # I dont need to write the getmax function I can maintain

        l = r = 0
        res = 0
        mymap = {}
        curmax = 0
        while r < len(s):
            mymap[s[r]] = mymap.get(s[r], 0) + 1
            curmax = max(curmax, mymap[s[r]])

            while not (r - l + 1 <= curmax + k):
                mymap[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)

            r += 1

        return res