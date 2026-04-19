class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1map = {}
        for ch in s1:
            s1map[ch] = s1map.get(ch, 0) + 1

        # abc # abcd
        size = len(s1)
        for i in range(len(s2) - size + 1):
            s2map = {}
            cur = s2[i:i+size]

            for ch in cur:
                s2map[ch] = s2map.get(ch, 0) + 1
            
            # (O(26) operation)
            if s2map == s1map:
                return True

        return False


            