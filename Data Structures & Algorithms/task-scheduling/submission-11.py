class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        minHeap = [-c for c in count.values()]
        heapq.heapify(minHeap)

        cooling = deque() # [time, count]
        time = 0

        while minHeap or cooling:
            time += 1

            if cooling and time == cooling[0][0]:
                heapq.heappush(minHeap, cooling.popleft()[1])
            
            if minHeap:
                c = heapq.heappop(minHeap) + 1

                if c != 0:
                    cooling.append([time + n + 1, c])
        
        return time