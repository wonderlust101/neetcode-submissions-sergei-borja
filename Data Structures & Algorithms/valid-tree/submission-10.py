class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parents = list(range(n))
        length = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        for a, b in edges:
            ra, rb = find(a), find(b)

            if ra == rb:
                return False

            if length[ra] < length[rb]:
                ra, rb = rb, ra
            
            parents[rb] = ra
            length[ra] += length[rb]

        return True