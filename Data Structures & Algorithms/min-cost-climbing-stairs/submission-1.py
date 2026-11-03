class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_back, two_back = 0, 0

        for i in range(2, len(cost) + 1):
            one_back, two_back = min(one_back + cost[i - 1], two_back + cost[i - 2]), one_back
        
        return one_back