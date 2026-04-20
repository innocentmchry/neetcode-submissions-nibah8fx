class Solution:

    def encode(self, strs: List[str]) -> str:
        # put hash as end identifier
        res = ""
        for i in range(len(strs)):
            res = res + str(len(strs[i])) + '#' + strs[i]
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        i = 0
        while i < len(s):
            l = i
            while s[i] != '#':
                i += 1
            
            size = int(s[l:i])
            res.append(s[i + 1:i + size + 1])
            i = i + size + 1
        
        return res
