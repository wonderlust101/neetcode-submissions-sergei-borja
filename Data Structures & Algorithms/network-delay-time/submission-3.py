class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t)) # dst, time
        
        res = 0
        minHeap = [(0, k)] # cost, dest
        visited = set()

        while minHeap:
            cost1, node1 = heapq.heappop(minHeap)

            if node1 in visited:
                continue
            
            visited.add(node1)
            res = cost1

            for node2, cost2 in adj[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (cost1 + cost2, node2))
        
        return res if len(visited) == n else -1