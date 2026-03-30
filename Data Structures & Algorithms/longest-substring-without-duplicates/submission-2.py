class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Let me do the brute force way first
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        res = 1
        for i in range(len(s)-1):
            my_set = set()
            my_set.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in my_set:
                    break
                else:
                    my_set.add(s[j])
            
            res = max(res, len(my_set))

        return res