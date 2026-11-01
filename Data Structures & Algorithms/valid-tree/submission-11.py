class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parents = list(range(n))
        length = [0] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        for a, b in edges:
            pa, pb = find(a), find(b)

            if pa == pb:
                return False
            
            if length[pa] < length[pb]:
                pa, pb = pb, pa

            parents[pb] = pa
            length[pa] += length[pb]
        
        return True