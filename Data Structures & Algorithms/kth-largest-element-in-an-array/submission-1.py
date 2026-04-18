class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # with minheap
        maxHeap = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, -nums[i])

        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1

        return -heapq.heappop(maxHeap)