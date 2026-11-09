class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in collections.Counter(tasks).values()]
        heapq.heapify(heap)

        cooling = deque() # [time, val]
        time = 0
        
        while heap or cooling:
            time += 1

            if cooling and cooling[0][0] == time:
                heapq.heappush(heap, cooling.popleft()[1])
            
            if heap:
                c = heapq.heappop(heap) + 1

                if c < 0:
                    cooling.append([time + n + 1, c])
            
        return time