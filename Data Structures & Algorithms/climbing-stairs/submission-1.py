class Solution:
    def climbStairs(self, n: int) -> int:
        one_back, two_back = 1, 1

        for i in range(n):
            one_back, two_back = one_back + two_back, one_back
        
        return two_back