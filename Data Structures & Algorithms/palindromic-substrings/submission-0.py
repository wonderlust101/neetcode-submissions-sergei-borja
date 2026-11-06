class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s) * 2 - 1):
            lo = i // 2
            hi = lo + i % 2

            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1
        
        return count