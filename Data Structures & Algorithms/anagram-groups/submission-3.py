class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for cur in strs:
            count = [0] * 26
            for ch in cur:
                count[ord(ch) - ord('a')] += 1

            res[tuple(count)].append(cur)
        
        return list(res.values())
