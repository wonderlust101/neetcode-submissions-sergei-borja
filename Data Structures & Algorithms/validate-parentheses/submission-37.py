class Solution:
    def isValid(self, s: str) -> bool:
        key = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for p in s:
            if p in key:
                if stack and stack[-1] == key[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return False if stack else True