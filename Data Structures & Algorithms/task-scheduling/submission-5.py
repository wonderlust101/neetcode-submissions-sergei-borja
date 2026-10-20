class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in collections.Counter(tasks).values()]
        heapq.heapify(heap)

        cooling = deque() # [time, count]
        time = 0

        while heap or cooling:
            time += 1

            if cooling and cooling[0][0] == time:
                heapq.heappush(heap, cooling.popleft()[1])

            if heap:
                count = heapq.heappop(heap) + 1

                if count:
                    cooling.append([time + n + 1, count])
        
        return time