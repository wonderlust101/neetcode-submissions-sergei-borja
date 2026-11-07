class Solution:
    def numDecodings(self, s: str) -> int:
        two_back, one_back  = 0, 1

        for i in range(len(s)):
            new = 0

            if s[i] != "0":
                new += one_back
            
            if i > 0 and "10" <= s[i - 1: i + 1] <= "26":
                new += two_back
            
            one_back, two_back = new, one_back
        
        return one_back