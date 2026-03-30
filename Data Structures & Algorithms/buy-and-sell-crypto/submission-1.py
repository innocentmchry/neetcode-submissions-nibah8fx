class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        left, right = 0, 1
        cur_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            
            right += 1
            cur_profit = max(cur_profit, profit)

        return cur_profit


