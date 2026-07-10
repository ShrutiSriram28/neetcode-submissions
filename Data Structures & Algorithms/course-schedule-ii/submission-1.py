class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        q = deque()
        order = []

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for i in range(len(indegree)):
            if not indegree[i]:
                q.append(i)
                order.append(i)
        
        while q:
            course = q.popleft()

            for c in graph[course]:
                if indegree[c]:
                    indegree[c] -= 1
                    if not indegree[c]:
                        q.append(c)
                        order.append(c)

        return order if len(order) == numCourses else []