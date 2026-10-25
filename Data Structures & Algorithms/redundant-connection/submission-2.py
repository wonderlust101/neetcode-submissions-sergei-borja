class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        count = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = find(parent[x])
                x = parent[x]
            return x
        
        for a, b in edges:
            ra, rb = find(a), find(b)

            if ra == rb:
                return [a, b]
            
            if count[ra] < count[rb]:
                ra, rb = rb, ra
            
            parent[rb] = ra
            count[ra] += 1