class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDict = [0] * 26

        for l in s:
            letterDict[ord(l) - ord("a")] += 1

        for l in t:
            letterDict[ord(l) - ord("a")] -= 1

        for i in letterDict:
            if i != 0:
                return False

        return True