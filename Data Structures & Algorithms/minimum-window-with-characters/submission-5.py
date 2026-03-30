class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_map, target_map = {}, {}
        for item in t:
            target_map[item] = target_map.get(item, 0) + 1

        l = 0
        have, need = 0, len(target_map) # even if it contains duplicates we are only tracking have == need. we do the rest in comparing = in maps
        res = [-1, -1] #, i,j
        min_res = float('inf')
        # i is r or right
        for i in range(len(s)):
            # cur_map[s[i]] = cur_map.get(s[i], 0) + 1
            if s[i] in target_map:
                cur_map[s[i]] = cur_map.get(s[i], 0) + 1
                if cur_map[s[i]] == target_map[s[i]]:
                    have += 1

            # if s[i] in target_map and cur_map[s[i]] == target_map[s[i]]:
            #     cur_map[s[i]] = cur_map.get(s[i], 0) + 1
            #     have += 1

            while have == need:
                w_size = i - l + 1
                if w_size < min_res:
                    res = [l, i]
                    min_res = w_size
                
                # cur_map[s[l]] -= 1
                if s[l] in cur_map:
                    cur_map[s[l]] -= 1

                if s[l] in target_map and cur_map[s[l]] < target_map[s[l]]:
                    have -=1

                l += 1
        
        l1, r1 = res
        return s[l1: r1+1] if min_res != float('inf') else ""
