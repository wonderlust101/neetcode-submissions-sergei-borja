class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0

        l = 0
        for r, ch in enumerate(s):
            if ch in seen:
                l = max(seen[ch] + 1, l)
            
            res = max(res, r - l + 1)
            seen[ch] = r
        
        return res