class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                cur_max = max(cur_max, prices[j] - prices[i])

        return cur_max
                
