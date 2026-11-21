class Solution:
    def climbStairs(self, n: int) -> int:
        twoBack, oneBack = 1, 1

        for i in range(n):
            twoBack, oneBack = oneBack, oneBack + twoBack
        
        return twoBack