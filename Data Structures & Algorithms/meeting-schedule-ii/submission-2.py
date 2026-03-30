"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        ptr1, ptr2 = 0, 0
        cur_meetings, res = 0, 0
        while ptr1 < len(start):
            if start[ptr1] < end[ptr2]:
                cur_meetings += 1
                ptr1 += 1
            else:
                # this means one metting ended and i can put the new meeting here
                cur_meetings -= 1
                ptr2 += 1
            
            res = max(cur_meetings, res)

        return res