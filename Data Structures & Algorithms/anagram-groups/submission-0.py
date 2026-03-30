class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Very important concept. sort() doesnt work because strings are immutable
        # Since sorted() returns a new list it can be used on any iterable.

        my_hashmap = {}
        res = []
        idx = 0
        for i in range(len(strs)):
            word = strs[i]
            alph = ''.join(sorted(word))
            if alph in my_hashmap:
                t_idx = my_hashmap[alph]
                res[t_idx].append(word)
            else:
                my_hashmap[alph] = idx
                idx += 1
                res.append([word])

        return res