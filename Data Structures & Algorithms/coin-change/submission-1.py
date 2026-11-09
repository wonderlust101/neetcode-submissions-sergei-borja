class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = [INF] * (amount + 1)
        dp[0] = 0
        
        for a in range(amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        print(dp)
        return dp[amount] if dp[amount] != INF else -1