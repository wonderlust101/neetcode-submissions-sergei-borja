class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 # total profit

        l, r = 0,0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > 0:
                res = max(res, profit)
            else:
                l = r
            
            r+=1

        return res