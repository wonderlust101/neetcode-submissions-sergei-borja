class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        L = 0

        for R in range(len(s)):
            if s[R] in seen and seen[s[R]] >= L:
                L = seen[s[R]] + 1

            seen[s[R]] = R
            res = max(res, R - L +1)

        return res