class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        q = deque(c for c in range(numCourses) if indegree[c] == 0)
        order = []
        while q:
            c = q.popleft()

            order.append(c)

            for nxt in adj[c]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return order if len(order) == numCourses else []
