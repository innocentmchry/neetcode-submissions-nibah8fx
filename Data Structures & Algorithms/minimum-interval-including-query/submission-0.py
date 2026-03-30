class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = []
        for q in queries:
            flag = False
            minimum = 10000
            for interval in intervals:            
                if interval[0] <= q <= interval[1]:
                    curr_min = interval[1] - interval[0] + 1
                    if curr_min < minimum:
                        minimum = curr_min
                        flag = True
                
            if flag == True:
                res.append(minimum)
            else:
                res.append(-1)
            

        return res