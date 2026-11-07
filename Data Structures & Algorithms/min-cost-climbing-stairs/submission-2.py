class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_back, one_back = 0, 0

        for i in range(2, len(cost) + 1):
            two_back, one_back = one_back, min(two_back + cost[i - 2], one_back + cost[i - 1])
        
        return one_back