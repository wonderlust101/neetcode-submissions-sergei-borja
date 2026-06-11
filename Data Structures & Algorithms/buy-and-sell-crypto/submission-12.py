class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0,0

        max_profit = 0
        while R < len(prices):
            profit = prices[R] - prices[L]
            
            if profit < 0:
                L = R
            
            R += 1

            max_profit = max(max_profit, profit)

        return max_profit