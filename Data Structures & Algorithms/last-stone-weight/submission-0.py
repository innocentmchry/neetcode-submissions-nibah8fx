class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        while len(maxHeap) > 1:
            l1 = heapq.heappop_max(maxHeap)
            l2 = heapq.heappop_max(maxHeap)
            if l1 - l2 != 0:
                heapq.heappush_max(maxHeap, l1 - l2)

        if len(maxHeap) == 1:
            return heapq.heappop_max(maxHeap)
        
        return 0