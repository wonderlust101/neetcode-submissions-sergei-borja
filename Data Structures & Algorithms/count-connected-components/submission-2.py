class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [p for p in range(n)]

        def find(x):
            while x != parent[x]:
                parent[x] = find(parent[x])
                x = parent[x]
            return x
        
        count = n
        for a, b in edges:
            pa, pb = find(a), find(b)

            if pa == pb:
                continue
            parent[pb] = pa
            
            count -= 1
        
        return count