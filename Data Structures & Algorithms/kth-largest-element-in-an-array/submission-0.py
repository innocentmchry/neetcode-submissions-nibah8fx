class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums
        heapq.heapify_max(maxHeap)

        while k > 1:
            heapq.heappop_max(maxHeap)
            k -= 1
        
        return heapq.heappop_max(maxHeap)
        