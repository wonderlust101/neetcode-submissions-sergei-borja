class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letter_freq = [0] * 26
        window_freq = [0] * 26

        for i in range(len(s1)):
            letter_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if letter_freq == window_freq:
                return True
            
            window_freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            if r < len(s2):
                window_freq[ord(s2[r]) - ord('a')] += 1
        
        return False