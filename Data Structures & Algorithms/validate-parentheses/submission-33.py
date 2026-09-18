class Solution:
    def isValid(self, s: str) -> bool:
        parenKey = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for paren in s:
            if paren in parenKey:
                if stack and parenKey[paren] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(paren)

        return not stack