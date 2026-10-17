class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def go(o, c):
            if len(path) == n * 2:
                res.append("".join(path[:]))
                return 
                
            if o < n:
                path.append("(")
                go(o + 1, c)
                path.pop()
            
            if c < o:
                path.append(")")
                go(o, c + 1)
                path.pop()

        go(0, 0)
        return res