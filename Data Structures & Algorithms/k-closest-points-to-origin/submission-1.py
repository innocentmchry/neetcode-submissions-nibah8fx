class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap question
        # O(n) for heapify
        myheap = []
        for coord in points:
            x, y = coord
            dist = x ** 2 + y ** 2
            heapq.heappush(myheap, ((dist, [x, y])))

        res = []
        for i in range(k):
            value, dist = heapq.heappop(myheap)
            res.append(dist)

        return res