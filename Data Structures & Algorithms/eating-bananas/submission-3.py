class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mymax = max(piles)
        mymin = mymax
        l = 1
        r = mymax
        while l <= r:
            mid = (l + r) // 2

            time = 0
            for p in piles:
                time += math.ceil(p/mid)

            if time <= h:
                mymin = min(mymin, mid)
                r = mid - 1
            else:
                l = mid + 1

        return mymin
