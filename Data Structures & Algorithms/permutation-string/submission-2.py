class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm_freq = [0] * 26
        curr_freq = [0] * 26
        l = 0

        # create perm_freq
        for letter in s1:
            perm_freq[ord(letter) - ord('a')] += 1
        
        # look through string
        for r in range(0, len(s2)):
            curr_freq[ord(s2[r]) - ord('a')] += 1
        
            if r - l == len(s1):
                curr_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if perm_freq == curr_freq:
                return True

        return False