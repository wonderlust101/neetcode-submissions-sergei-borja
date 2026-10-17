class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        path = []

        KEYS = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # The index is the first letter
        def dfs(i):
            if i == len(digits):
                res.append(''.join(path[:]))
                return 

            # goes through each letter in wheel
            for c in KEYS[digits[i]]:
                path.append(c)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return res