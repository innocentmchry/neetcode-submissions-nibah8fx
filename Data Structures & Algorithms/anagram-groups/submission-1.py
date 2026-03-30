class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        # count = [] # 0 - 25, value of 'a' is 97

        def ret_key(word):
            count = [0] * 26
            for ch in word:
                asci_value_normalized = 97 - ord(ch)
                count[asci_value_normalized] += 1

            return tuple(count)
        
        res = []
        idx = 0
        for cur in strs:
            k = ret_key(cur)
            if k in my_map:
                t_idx = my_map[k]
                res[t_idx].append(cur)
            else:
                my_map[k] = idx
                idx += 1
                res.append([cur])

        return res