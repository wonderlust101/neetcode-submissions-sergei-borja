class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for l in s:
            count[ord(l) - ord('a')] += 1
        
        for l in t:
            count[ord(l) - ord('a')] -= 1
        
        for c in count:
            if c != 0:
                return False
        
        return True