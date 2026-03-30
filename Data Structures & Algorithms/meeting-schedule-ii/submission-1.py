"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        if len(intervals) == 0:
            return 0
        
        res = []
        res.append(intervals[0].end)
        for i in range(1, len(intervals)):
            cur_l, cur_r = intervals[i].start, intervals[i].end
            
            flag = 0
            for j in range(len(res)):
                if cur_l >= res[j]:
                    res[j] = cur_r
                    flag = 1
                    break

            if flag == 0:
                res.append(cur_r)

        return len(res)
