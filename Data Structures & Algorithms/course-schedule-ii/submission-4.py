class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlocks = [[] for _ in range(numCourses)]
        waitsFor = [0] * numCourses

        for course, pre in prerequisites:
            unlocks[pre].append(course)
            waitsFor[course] += 1

        q = deque(c for c in range(numCourses) if waitsFor[c] == 0)
        order = []
        while q:
            c = q.popleft()
            order.append(c)

            for nxt in unlocks[c]:
                waitsFor[nxt] -= 1

                if waitsFor[nxt] == 0:
                    q.append(nxt)
        
        return order if len(order) == numCourses else []