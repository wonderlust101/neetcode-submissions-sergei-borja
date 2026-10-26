class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        length = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = find(parent[x])
                x = parent[x]
            
            return x
        
        count = n
        for a, b in edges:
            ra, rb = find(a), find(b)

            if ra == rb:
                continue
            
            if length[ra] < length[rb]:
                ra, rb = rb, ra
            
            parent[rb] = ra
            length[ra] += rb
            count -= 1
        
        return count