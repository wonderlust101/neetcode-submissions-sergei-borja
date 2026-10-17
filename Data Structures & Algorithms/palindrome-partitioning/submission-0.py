class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def explore(start):
            # Append to res if start reach the end of string`
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                # Gets part of the string
                piece = s[start: i + 1]

                # Continue if that part is not a palindrome
                if piece != piece[::-1]:
                    continue

                path.append(piece)
                explore(i + 1)
                path.pop()
        
        explore(0)
        return res