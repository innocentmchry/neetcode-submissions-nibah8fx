class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)

        for n in nums:
            my_map[n] += 1
        
        # my_heap = list(my_map.items())
        # my_heap = [(x[1], x[0]) for x in my_heap]
        my_heap = [(freq, num) for num, freq in my_map.items()]

        heapq.heapify_max(my_heap)

        # res = []
        # for i in range(k):
        #     res.append((heapq.heappop_max(my_heap))[1])
        
        return [heapq.heappop_max(my_heap)[1] for _ in range(k)]