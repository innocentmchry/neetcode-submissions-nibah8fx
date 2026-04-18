class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        myset = set()
        res = 1

        for i in range(len(s)):
            if s[i] not in myset:
                myset.add(s[i])
                res = max(res, len(myset))
            else:
                while s[i] in myset:
                    myset.remove(s[left])
                    left += 1
                myset.add(s[i])

        return res
