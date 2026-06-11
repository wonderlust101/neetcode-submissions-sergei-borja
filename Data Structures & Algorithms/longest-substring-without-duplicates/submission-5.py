class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char = set()
        L, R = 0,0
        max_len = 0

        while R < len(s):
            while s[R] in unique_char:
                unique_char.remove(s[L])
                L += 1
            
            unique_char.add(s[R])
            max_len = max(max_len, len(unique_char))
            R += 1

        return max_len