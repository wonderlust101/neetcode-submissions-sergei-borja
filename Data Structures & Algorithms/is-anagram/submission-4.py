class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_count = {}

        for i in range(len(s)):
            letter_count[s[i]] = 1 + letter_count.get(s[i], 0)
            letter_count[t[i]] = letter_count.get(t[i], 0) - 1

        for i in letter_count:
            if letter_count[i] != 0:
                return False
        
        return True