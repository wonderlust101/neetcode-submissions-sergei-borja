class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_hash = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            # while there is a dup
            while s[r] in char_hash:
                char_hash.remove(s[l])
                l += 1

            # otherwise, add to hash
            char_hash.add(s[r])
            r += 1

            # get max len
            res = max(res, len(char_hash))
        
        return res