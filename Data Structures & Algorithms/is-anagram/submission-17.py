class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = [0] * 26

        for letter in s:
            letter_count[ord(letter) - ord("a")] += 1
        
        for letter in t:
            letter_count[ord(letter) - ord("a")] -= 1
        
        for count in letter_count:
            if count != 0:
                return False
        
        return True