class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        length = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        count = n
        for x, y in edges:
            px, py = find(x), find(y)

            if px == py:
                continue
            
            if length[px] < length[py]:
                px, py = py, px

            parent[py] = px
            length[px] += length[py]

            count -= 1
        
        return count