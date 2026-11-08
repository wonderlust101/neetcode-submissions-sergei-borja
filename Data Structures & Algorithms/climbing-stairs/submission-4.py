class Solution:
    def climbStairs(self, n: int) -> int:
        two_back, one_back = 1, 1

        for i in range(n):
            two_back, one_back = one_back, one_back + two_back
        
        return two_back