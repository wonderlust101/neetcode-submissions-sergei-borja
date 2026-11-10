class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        length = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in edges:
            px, py = find(x), find(y)

            if px == py:
                return False
            
            if length[px] < length[py]:
                px, py = py, px

            parent[py] = px
            length[px] += length[py]
        
        return True