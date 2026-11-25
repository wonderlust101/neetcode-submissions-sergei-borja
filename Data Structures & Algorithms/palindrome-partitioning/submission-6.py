class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start):
            if start == len(s):
                res.append(path[::])
                return
            
            for end in range(start, len(s)):
                partition = s[start: end + 1]

                if not partition == partition[::-1]:
                    continue
                
                path.append(partition)
                dfs(end + 1)
                path.pop()

        dfs(0)
        return res