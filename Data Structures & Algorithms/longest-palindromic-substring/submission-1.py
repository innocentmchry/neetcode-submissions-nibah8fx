class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        def palindrome(l, r):
            nonlocal res, reslen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i
            palindrome(l, r)

            l, r = i, i+1
            palindrome(l, r)

        return res
            