class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0

        l, r = 0, 1
        best = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            
            best = max(profit, best)
            r += 1

        return best