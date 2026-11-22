class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        bestL, bestR = 0, 0

        def check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return l + 1, r - 1
        
        for i in range(len(s)):
            for l, r in (check(i,i), check(i, i + 1)):
                if r - l > bestR - bestL:
                    bestL, bestR = l, r
        
        return s[bestL: bestR + 1]