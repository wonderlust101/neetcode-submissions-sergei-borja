class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26

        for l in s:
            alpha[ord(l) - ord("a")] += 1
        
        for l in t:
            alpha[ord(l) - ord("a")] -= 1

        for i in alpha:
            if i != 0:
                return False
        return True