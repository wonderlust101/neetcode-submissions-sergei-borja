class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlocks = [[] for _ in range(numCourses)]
        waits_on = [0] * numCourses

        for course, pre in prerequisites:
            unlocks[pre].append(course)
            waits_on[course] += 1
        
        line = deque(c for c in range(numCourses) if waits_on[c] == 0)
        order = []
        while line:
            c = line.popleft()
            order.append(c)

            for nxt in unlocks[c]:
                waits_on[nxt] -= 1

                if waits_on[nxt] == 0:
                    line.append(nxt)
        
        return order if len(order) == numCourses else []
        
