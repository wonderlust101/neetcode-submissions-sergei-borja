class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(n + 1))
        length = [1] * (n + 1)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        for a, b in edges:
            pa, pb = find(a), find(b)

            if pa == pb:
                return [a, b]
            
            if length[pa] < length[pb]:
                pa, pb = pb, pa
            
            parents[pb] = pa
            length[pa] += length[pb]
        
