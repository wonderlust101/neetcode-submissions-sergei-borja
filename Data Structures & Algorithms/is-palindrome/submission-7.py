class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_pointer = 0
        r_pointer = len(s) - 1

        while l_pointer < r_pointer:
            while l_pointer < r_pointer and not s[l_pointer].isalnum():
                l_pointer += 1

            while l_pointer < r_pointer and not s[r_pointer].isalnum():
                r_pointer -= 1
            
            if s[l_pointer].lower() != s[r_pointer].lower():
                return False

            l_pointer += 1
            r_pointer -= 1

        return True