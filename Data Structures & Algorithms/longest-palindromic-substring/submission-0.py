class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo_max, hi_max = 0, 0

        def dfs(lo, hi):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1

            return lo + 1, hi - 1
        
        for i in range(len(s)):
            for lo, hi in (dfs(i, i), dfs(i, i + 1)):
                if hi - lo > hi_max - lo_max:
                    lo_max, hi_max = lo, hi
        
        return s[lo_max: hi_max + 1]
