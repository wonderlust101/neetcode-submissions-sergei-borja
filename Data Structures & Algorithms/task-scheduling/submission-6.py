class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [-c for c in collections.Counter(tasks).values()]
        heapq.heapify(counter)

        cooling = deque() # [time, counter]
        time = 0
        while counter or cooling:
            time += 1

            if cooling and cooling[0][0] == time:
                heapq.heappush(counter, cooling.popleft()[1])
            
            if counter:
                c = heapq.heappop(counter) + 1

                if c < 0:
                    cooling.append([time + n + 1, c])

        return time