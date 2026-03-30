class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Now i will do in efficient way O(n)
        # Using Sliding window and set
        # Brainfuck logic nice concept
        if len(s) == 0:
            return 0

        my_set = set()
        left = 0
        res = 1
        for i in range(len(s)):
            if s[i] not in my_set:
                my_set.add(s[i])
                res = max(len(my_set), res)
            else:
                while s[i] in my_set:
                    my_set.remove(s[left])
                    left += 1
                my_set.add(s[i])

        return res