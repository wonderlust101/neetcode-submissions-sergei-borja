class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # 
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        # Searches for the parent
        def find(x):
            while parent[x] != x:
                # Half path compression
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        for a, b in edges:
            ra, rb = find(a), find(b)

            if ra == rb:
                return [a, b]
            
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            
            parent[rb] = ra
            size[ra] += size[rb]