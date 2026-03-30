class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = [0] * 26
        count_2 = [0] * 26

        for ch in s:
            idx = ord(ch)
            count_1[ord(ch) - ord('a')] += 1
        
        for ch in t:
            idx = ord(ch)
            count_2[ord(ch) - ord('a')] += 1
        
        if count_1 == count_2:
            return True
        else:
            return False
            

