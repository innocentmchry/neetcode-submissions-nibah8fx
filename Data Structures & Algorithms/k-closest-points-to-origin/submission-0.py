import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ls = []

        for pt in points:
            x, y = pt

            ls.append(((x * x + y * y), [x,y]))

        heapq.heapify(ls)

        res = []

        for i in range(k):
            res.append(heapq.heappop(ls)[1])

        return res


