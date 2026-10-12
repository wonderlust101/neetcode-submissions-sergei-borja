class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in collections.Counter(tasks).values()]
        heapq.heapify(heap)

        cooling = deque()
        t = 0

        while heap or cooling:
            t += 1

            if cooling and cooling[0][1] <= t: # cooldown over
                heapq.heappush(heap, cooling.popleft()[0])
            
            if heap: # run task with most copies left
                left = heapq.heappop(heap) + 1

                if left: # if still less than 0
                    cooling.append((left, t + n + 1))

            # otherwise, idle
        
        return t

