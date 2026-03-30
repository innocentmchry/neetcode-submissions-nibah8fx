class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort solution

        my_map = {}
        for num in nums:
            my_map[num] = 1 + my_map.get(num, 0) # interesting way to initialize

        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in my_map.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            # very interesting. its like for n in [] which is empty so python skips it
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
