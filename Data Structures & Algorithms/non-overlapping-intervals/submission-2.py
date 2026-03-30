class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort()
        count = 0
        prev_r = intervals[0][1]
        for i in range(1, len(intervals)):
            cur_l, cur_r = intervals[i]
            if cur_l < prev_r:
                prev_r = min(cur_r, prev_r)
                count += 1
            else:
                prev_r = cur_r

        return count

        