class Solution:
    def isValid(self, s: str) -> bool:
        parenKey = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        parenStack = []

        for paren in s:
            if paren in parenKey:
                if parenStack and parenStack[-1] == parenKey[paren]:
                    parenStack.pop()
                else:
                    return False
            else:
                parenStack.append(paren)

        return not parenStack