class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def explore(o, c):
            if len(path) == n * 2:
                res.append("".join(path[:]))
                return
            
            if o < n:
                path.append("(")
                explore(o + 1, c)
                path.pop()

            if c < o:
                path.append(")")
                explore(o, c + 1)
                path.pop()
        
        explore(0, 0)
        return res