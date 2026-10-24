class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        roads = [[] for _ in range(n)]

        for a, b in edges:
            roads[a].append(b)
            roads[b].append(a)
        
        seen = {0}
        stack = [0]

        while stack:
            town = stack.pop()

            for nxt in roads[town]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        
        return len(seen) == n