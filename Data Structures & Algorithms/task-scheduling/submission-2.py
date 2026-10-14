class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = [-c for c in counter.values()]

        heapq.heapify(heap)

        cooling = deque() # [time, val]
        time = 0

        while heap or cooling:
            time += 1

            if cooling and cooling[0][0] == time:
                t, val = cooling.popleft()
                heapq.heappush(heap, val)
            
            if heap:
                val = heapq.heappop(heap) + 1

                if val < 0:
                    cooling.append([time + n + 1, val])
        
        return time
