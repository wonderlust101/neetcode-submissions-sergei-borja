class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False
        
        parent = list(range(n))
        length = [1] * n

        def find(x):
            while parent[x] != x:
                x = find(parent[x])
            return x
        
        for x, y in edges:
            px, py = find(x), find(y)

            if px == py:
                return False
            
            if length[px] < length[py]:
                px, py = py, px
            
            parent[py] = px
            length[px] += length[py]
        
        return True
            