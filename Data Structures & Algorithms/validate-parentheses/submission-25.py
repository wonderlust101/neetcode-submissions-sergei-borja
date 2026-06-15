class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # key p
        p_key = {
            "]": "[",
            "}": "{",
            ")": "(",
        }

        for p in s:
            if p in p_key:
                if stack and p_key[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return False if stack else True