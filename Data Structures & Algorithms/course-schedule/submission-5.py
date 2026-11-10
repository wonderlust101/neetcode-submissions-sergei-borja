class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unlocks = [[] for _ in range(numCourses)]
        waitsFor = [0] * numCourses

        for course, pre in prerequisites:
            unlocks[pre].append(course)
            waitsFor[course] += 1

        q = deque(c for c in range(numCourses) if waitsFor[c] == 0)
        count = 0

        while q:
            c = q.popleft()

            count += 1

            for nxt in unlocks[c]:
                waitsFor[nxt] -= 1

                if waitsFor[nxt] == 0:
                    q.append(nxt)
        
        return numCourses == count