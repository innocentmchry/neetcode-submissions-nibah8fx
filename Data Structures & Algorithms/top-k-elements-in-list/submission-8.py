class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = Counter(nums)
        mydict = {}
        for n in nums:
            mydict[n] = mydict.get(n, 0) + 1

        maxheap = []
        for key, val in mydict.items():
            heapq.heappush_max(maxheap, (val, key))

        res = []
        for i in range(k):
            res.append(heapq.heappop_max(maxheap)[1])

        return res