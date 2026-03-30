class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)

        for n in nums:
            my_map[n] += 1
        
        my_heap = list(my_map.items())
        my_heap = [(x[1], x[0]) for x in my_heap]

        heapq.heapify_max(my_heap)
        print(my_heap)
        res = []
        for i in range(k):
            res.append((heapq.heappop_max(my_heap))[1])
        
        return res