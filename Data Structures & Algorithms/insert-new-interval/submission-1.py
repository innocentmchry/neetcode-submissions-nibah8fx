class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            curr_l, curr_r = intervals[i]

            interval_l, interval_r = newInterval

            if interval_r < curr_l:
                res.append(newInterval)
                return res + intervals[i:]
            elif interval_l > curr_r:
                res.append(intervals[i])
            else:
                newInterval = [min(curr_l, interval_l), max(curr_r, interval_r)]

        res.append(newInterval)
        return res


