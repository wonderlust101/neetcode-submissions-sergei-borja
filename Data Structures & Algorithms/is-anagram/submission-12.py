class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq = [0] * 26

        for l in s:
            letter_freq[ord(l) - ord('a')] += 1

        for l in t:
            letter_freq[ord(l) - ord('a')] -= 1

        for num in letter_freq:
            if num != 0:
                return False
        
        return True