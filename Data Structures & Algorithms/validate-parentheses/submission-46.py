class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenKey = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        
        for p in s:
            if p in parenKey:
                if stack and stack[-1] == parenKey[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return True if not stack else False