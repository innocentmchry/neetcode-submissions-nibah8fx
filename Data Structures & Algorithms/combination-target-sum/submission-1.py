class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        cur = []

        def dfs(start, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            
            for i in range(len(nums)):
                cur.append(nums[i])
                dfs(i, total + nums[i])
                cur.pop()

        dfs(0,0)

        unique = {}

        for lst in res:
            key = tuple(sorted(Counter(lst).items()))
            if key not in unique:
                unique[key] = lst

        return list(unique.values())

        # Notes: Counter(ls) returns a counter object similar to dictionary
        #        .items() is anyways required in iteration for both key and value
        #        need to convert it to tuple to store it as a key (since sorted returns list)
        #        if you sort a dictionary it sorts key first then value based on unicode and returns a list :x


        
