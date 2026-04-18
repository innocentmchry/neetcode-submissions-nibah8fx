class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxheap + queue solution. I think its a very good question
        counts = Counter(tasks) # A:3, B:2 etc
        maxHeap = []
        for value in counts.values():
            heapq.heappush_max(maxHeap, value)
        
        time = 0
        q = collections.deque()

        while maxHeap or q:
            time += 1
            if len(maxHeap) > 0:
                cur = heapq.heappop_max(maxHeap)
                if cur - 1 > 0:
                    q.append([cur - 1, time + n])

            if q and q[0][1] == time:
                topush = q.popleft()
                heapq.heappush_max(maxHeap, topush[0])

        return time





