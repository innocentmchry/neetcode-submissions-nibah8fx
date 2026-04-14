class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minvalue = r

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
                
            if hours <= h and mid < minvalue:
                minvalue = mid

            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
            
        return minvalue