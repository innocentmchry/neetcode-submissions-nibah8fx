class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_1 = [0] * 26
        count_2 = [0] * 26

        for i in range(len(s)):
            count_1[ord(s[i]) - ord('a')] += 1
            count_2[ord(t[i]) - ord('a')] += 1

        return count_1 == count_2
            

