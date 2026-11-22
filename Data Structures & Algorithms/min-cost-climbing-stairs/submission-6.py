class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        oneBack, twoBack = 0, 0

        for i in range(2, len(cost) + 1):
            oneBack, twoBack = min(oneBack + cost[i - 1], twoBack + cost[i - 2]), oneBack
        
        return oneBack