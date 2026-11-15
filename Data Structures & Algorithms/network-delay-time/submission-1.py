class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, tar, time in times:
            adj[src].append((tar, time))

        minHeap = [(0, k)]
        time = 0
        visited = set()

        while minHeap:
            time1, tar1 = heapq.heappop(minHeap)

            if tar1 in visited:
                continue
            
            visited.add(tar1)
            time = time1

            for tar2, time2 in adj[tar1]:
                if tar2 not in visited:
                    heapq.heappush(minHeap, (time1 + time2, tar2))
        
        return time if len(visited) == n else -1
