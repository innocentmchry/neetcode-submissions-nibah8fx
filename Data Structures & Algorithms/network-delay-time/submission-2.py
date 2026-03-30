class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = collections.defaultdict(list) # its an adjacency list

        for i in range(len(times)):
            u1, u2, w = times[i]
            edges[u1].append((u2, w))

        minHeap = [(0, k)] # starting node
        visited = set()
        t = 0

        while minHeap:
            w, tn = heapq.heappop(minHeap)
            if tn in visited:
                continue

            t = max(t, w)
            
            visited.add(tn)

            for edge in edges[tn]:
                cu2, cw = edge
                if cu2 not in visited:
                    heapq.heappush(minHeap, (w + cw, cu2))

        if len(visited) == n:
            return t
        else:
            return -1

