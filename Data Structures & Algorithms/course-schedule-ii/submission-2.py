class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlocks = [[] for _ in range(numCourses)]
        waitsOn = [0] * numCourses

        for course, pre in prerequisites:
            unlocks[pre].append(course)
            waitsOn[course] += 1
        
        q = deque(c for c in range(numCourses) if waitsOn[c] == 0)
        res = []
        while q:
            c = q.popleft()
            res.append(c)

            for nxt in unlocks[c]:
                waitsOn[nxt] -= 1

                if waitsOn[nxt] == 0:
                    q.append(nxt)
        
        return res if len(res) == numCourses else []