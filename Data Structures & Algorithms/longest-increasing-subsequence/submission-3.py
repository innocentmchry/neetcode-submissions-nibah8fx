class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ls = []
        if nums:
            ls.append(nums[0])

        for i in range(1, len(nums)):
            flag = False
            c = nums[i]
            for n in range(len(ls)):
                if c <= ls[n]:
                    ls[n] = c
                    flag = True
                    break
            if not flag:
                ls.append(c)

        return len(ls)