class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unlocks = [[] for _ in range(numCourses)]
        waits_on = [0] * numCourses

        for course, pre in prerequisites:
            unlocks[pre].append(course)
            waits_on[course] += 1
        
        line = deque(c for c in range(numCourses) if waits_on[c] == 0)
        taken = 0

        while line:
            c = line.popleft()
            taken += 1

            for nxt in unlocks[c]:
                waits_on[nxt] -= 1

                if waits_on[nxt] == 0:
                    line.append(nxt)
        
        return taken == numCourses