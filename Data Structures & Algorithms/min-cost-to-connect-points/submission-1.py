class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(1, n):
                x2, y2 = points[j]

                md = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((md, j))
                adj[j].append((md, i))
        
        minHeap = [(0, 0)] # cost, dst
        res = 0
        visited = set()

        while minHeap:
            cost, dst = heapq.heappop(minHeap)
            if dst in visited:
                continue
            
            visited.add(dst)
            res += cost

            for neiCost, nei in adj[dst]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiCost, nei))
        
        return res