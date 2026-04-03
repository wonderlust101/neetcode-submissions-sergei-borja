class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0
        
        for R in range(len(prices)):
            diff = prices[R] - prices[L]

            if diff <= 0:
                L = R

            res = max(res, diff)
        
        return res

            