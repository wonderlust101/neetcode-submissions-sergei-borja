class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict = [0] * 26

        for l in s:
            word_dict[ord(l) - ord('a')] += 1
        
        for l in t:
            word_dict[ord(l) - ord('a')] -= 1
        
        for n in word_dict:
            if n != 0:
                return False
        
        return True