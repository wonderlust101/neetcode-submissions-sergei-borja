class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def explore(start):
            if len(s) == start:
                res.append(path[:])
                return 
            
            for i in range(start, len(s)):
                split = s[start : i + 1]

                if split != split[::-1]:
                    continue
                
                path.append(split)
                explore(i + 1)
                path.pop()
        
        explore(0)
        return res