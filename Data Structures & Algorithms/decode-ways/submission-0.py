class Solution:
    def numDecodings(self, s: str) -> int:
        two_back, one_back = 0, 1

        for i in range(len(s)):
            new = 0
            if s[i] != "0":
                new += one_back
            if i >= 1 and '10' <= s[i-1:i+1] <= '26':
                new += two_back
            
            two_back, one_back = one_back, new
        
        return one_back