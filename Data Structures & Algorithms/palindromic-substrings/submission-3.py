class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s) *2):
            l = i // 2
            r = l + i % 2

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            
        return res