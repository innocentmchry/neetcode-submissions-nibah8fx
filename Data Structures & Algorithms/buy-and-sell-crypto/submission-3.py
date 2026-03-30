class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        left = 0
        for i in range(1, len(prices)):
            right = i
            cur_profit = prices[right] - prices[left]
            if cur_profit < 0:
                left = right
            
            profit = max(cur_profit, profit)

        return profit
            
