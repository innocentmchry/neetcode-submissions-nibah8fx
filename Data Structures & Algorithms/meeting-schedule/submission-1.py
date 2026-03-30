"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            prev_l, prev_r = intervals[i-1].start, intervals[i-1].end
            cur_l, right = intervals[i].start, intervals[i].end

            if prev_l <= cur_l < prev_r:
                return False
        
        return True