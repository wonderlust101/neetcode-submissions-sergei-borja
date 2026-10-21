class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(o, c):
            if len(path) == (n*2):
                res.append("".join(path[:]))
                return
            
            if o < n:
                path.append("(")
                dfs(o + 1, c)
                path.pop()
            
            if c < o:
                path.append(")")
                dfs(o, c + 1)
                path.pop()
        
        dfs(0, 0)
        return res