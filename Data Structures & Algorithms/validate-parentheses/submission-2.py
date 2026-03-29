class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        prevPar = []

        i = 0
        while i < len(s) - 1:
            if s[i] in parMap:
                if not parMap[s[i]] == prevPar[-1] or len(s) == 0:
                    return False

                prevPar.pop()
                i += 1
                continue

            prevPar.append(s[i])


            i += 1
        
        return True