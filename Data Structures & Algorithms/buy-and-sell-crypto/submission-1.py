class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0

        for R in range(len(prices)):
            profit = prices[R] - prices[L]

            if profit <= 0:
                L = R
                
            res = max(res, profit)

        return res