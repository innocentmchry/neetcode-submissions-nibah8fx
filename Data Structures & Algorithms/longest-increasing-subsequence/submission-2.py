class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        rows = []

        for i in range(len(nums)):
            flag = False
            if len(rows) == 0:
                rows.append([nums[i]])
            else:
                for j in range(len(rows)):
                    if rows[j][-1] >= nums[i]:
                        rows[j].append(nums[i])
                        flag = True
                        break
                if not flag:
                    rows.append([nums[i]])
                
        
        return len(rows)