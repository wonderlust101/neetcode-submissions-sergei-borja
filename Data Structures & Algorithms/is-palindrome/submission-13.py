class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # advance forward if not alpha
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            # check if not equal
            if s[l].lower() != s[r].lower():
                return False
            
            # move pointers
            l += 1
            r -= 1
        
        return True
