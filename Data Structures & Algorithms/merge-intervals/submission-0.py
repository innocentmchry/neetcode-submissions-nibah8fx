class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]

            if cur[0] > prev[1]:
                res.append(prev)
                prev = cur
            else:
                prev = [min(prev[0], cur[0]), max(prev[1], cur[1])]

        res.append(prev)
        return res