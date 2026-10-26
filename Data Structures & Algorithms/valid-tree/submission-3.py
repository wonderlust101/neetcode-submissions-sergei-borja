class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))
        length = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = find(parent[x])
                x = parent[x]
            
            return x
        
        for a, b in edges:
            ra, rb = find(a), find(b)

            if ra == rb:
                return False
            if length[ra] < length[rb]:
                ra, rb = rb, ra
            
            parent[rb] = ra
            length[ra] += length[rb]
        
        return True
