class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for l in s:
            count[ord(l) - ord('a')] += 1
        
        for l in t:
            count[ord(l) - ord('a')] -= 1

        for n in count:
            if n != 0:
                return False
        
        return True