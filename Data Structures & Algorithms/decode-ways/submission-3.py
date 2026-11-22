class Solution:
    def numDecodings(self, s: str) -> int:
        oneBack, twoBack = 1, 0

        for i in range(len(s)):
            new = 0

            if s[i] != "0":
                new += oneBack
            if i > 0 and "10" <= s[i - 1: i + 1] <= "26":
                new += twoBack

            oneBack, twoBack = new, oneBack
        
        return oneBack