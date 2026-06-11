class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_set = set()

        L = 0

        for R in range(len(s)):
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            
            char_set.add(s[R])
            res = max(res, len(char_set))
        
        return res