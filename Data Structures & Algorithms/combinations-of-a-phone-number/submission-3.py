class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        key = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res, path = [], []

        def explore(i):
            if len(path) == len(digits):
                res.append("".join(path[::]))
                return
            
            for ch in key[digits[i]]:
                path.append(ch)
                explore(i + 1)
                path.pop()
        
        explore(0)
        return res