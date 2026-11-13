class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for src, tar, t in times:
            edges[src].append((tar, t))

        minHeap = [(0, k)]
        time = 0
        visited = set()

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)

            if node1 in visited:
                continue

            visited.add(node1)
            time = time1

            for node2, time2 in edges[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (time1 + time2, node2))
            
        return time if len(visited) == n else -1