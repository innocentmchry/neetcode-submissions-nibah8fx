class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        res = []

        intervals.sort()
        prev_l, prev_r = intervals[0]
        for i in range(1, len(intervals)):
            cur_l, cur_r = intervals[i]
            if cur_l > prev_r:
                res.append([prev_l, prev_r])
                prev_l, prev_r = cur_l, cur_r
            else:
                prev_l, prev_r = min(prev_l, cur_l), max(prev_r, cur_r)

        res.append([prev_l, prev_r])
        return res
            
        