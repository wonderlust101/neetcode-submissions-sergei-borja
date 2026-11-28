class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        q = deque(c for c in range(numCourses) if indegree[c] == 0)
        count = 0
        while q:
            c = q.popleft()

            count += 1

            for nxt in adj[c]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return count == numCourses
