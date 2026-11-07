class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo_best, hi_best = 0, 0

        def dfs(lo, hi):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            
            return lo + 1, hi - 1
        
        for c in range(len(s)):
            for lo, hi in (dfs(c, c), dfs(c, c + 1)):
                if hi - lo > hi_best - lo_best:
                    lo_best, hi_best = lo, hi
        
        return s[lo_best : hi_best + 1]