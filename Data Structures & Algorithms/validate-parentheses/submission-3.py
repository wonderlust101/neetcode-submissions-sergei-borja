class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        prevPar = []

        i = 0
        while i < len(s):
            if s[i] in parMap:
                if not prevPar or not parMap[s[i]] == prevPar[-1]:
                    return False

                prevPar.pop()
                i += 1
                continue

            prevPar.append(s[i])


            i += 1
        
        return len(prevPar) == 0