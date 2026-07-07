class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        q = deque([])
        visited = []

        # b before a
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            visited.append(course)

            for pre in graph[course]:
                if pre not in visited:
                    indegree[pre] -= 1
                    if indegree[pre] == 0:
                        q.append(pre)

        return True if len(visited) == numCourses else False

                
