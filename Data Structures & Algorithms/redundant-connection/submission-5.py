class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        length = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in edges:
            px, py = find(x), find(y)

            if px == py:
                return [x, y]
            
            if length[px] < length[py]:
                px, py = py, px

            parent[py] = px
            length[px] += length[py]