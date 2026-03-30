class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        left, right = 0, 0

        def get_max(my_map):
            my_max = 0
            for value in my_map.values():
                if value > my_max:
                    my_max = value

            return my_max

        res = 0
        while right < len(s):
            count_map[s[right]] = count_map.get(s[right], 0) + 1
            
            cur_max_alphabet = get_max(count_map)

            if (right - left + 1 - cur_max_alphabet) <= k:
                res = max(right - left + 1, res)
            else:
                while not (right - left + 1 - get_max(count_map)) <= k:
                    count_map[s[left]] -= 1
                    left += 1
            
            right += 1
            


        return res
