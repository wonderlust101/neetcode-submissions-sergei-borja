class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def explore(start):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                splice = s[start : end + 1]

                if splice == splice[::-1]:
                    path.append(splice)
                    explore(end + 1)
                    path.pop()
        
        explore(0)
        return res