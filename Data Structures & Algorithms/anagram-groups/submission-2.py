class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            mydict[key].append(strs[i])

        return list(mydict.values())