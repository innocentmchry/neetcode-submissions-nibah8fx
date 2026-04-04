class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        def palindromes(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r+1])
                l -= 1
                r += 1

        for i in range(len(s)):
            l, r = i, i
            palindromes(l, r)
            l, r = i, i+1
            palindromes(l, r)

        return len(res)