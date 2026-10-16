class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0

        fMax = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            fMax = max(fMax, count[s[r]])

            while (r - l + 1) - fMax > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res