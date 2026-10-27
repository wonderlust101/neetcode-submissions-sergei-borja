class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxFreq = 0

        res = 0
        l = 0
        for r, ch in enumerate(s):
            count[ch] += 1
            maxFreq = max(maxFreq, count[ch])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res