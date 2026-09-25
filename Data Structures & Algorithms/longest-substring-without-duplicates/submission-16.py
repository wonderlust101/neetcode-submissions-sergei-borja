class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l) 
            
            seen[s[r]] = r
            r += 1
            res = max(res, r - l)
        
        return res