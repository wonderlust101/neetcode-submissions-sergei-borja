class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterFreq = [0] * 26

        for l in s:
            letterFreq[ord(l) - ord('a')] += 1

        for l in t:
            letterFreq[ord(l) - ord('a')] -= 1
        
        for i in letterFreq:
            if i != 0:
                return False
        
        return True