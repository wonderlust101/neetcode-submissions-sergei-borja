class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        l = 0

        for r, n in enumerate(s):
            if n in seen:
                l = max(seen[n] + 1, l)
            
            res = max(res, r - l + 1)
            seen[n] = r
        
        return res