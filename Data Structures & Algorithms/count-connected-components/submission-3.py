class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        length = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        count = n
        for a, b in edges:
            pa, pb = find(a), find(b)

            if pa == pb:
                continue
            
            if length[pa] < length[pb]:
                pa, pb = pb, pa
            
            parents[pb] = pa
            length[pa] += length[pb]
            count -= 1
        
        return count