class Solution:
    def isValid(self, s: str) -> bool:
        pKey = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for p in s:
            if p in pKey:
                if stack and stack[-1] == pKey[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return False if stack else True