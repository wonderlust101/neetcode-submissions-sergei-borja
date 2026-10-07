class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in count:
                l = max(count[s[r]] + 1, l)
            
            res = max(res, r - l + 1)
            count[s[r]] = r
            r += 1
        
        return res