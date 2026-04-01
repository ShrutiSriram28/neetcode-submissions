class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}

        for prereqs in prerequisites:
            graph[prereqs[0]].append(prereqs[1])

        visited = []

        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True

            visited.append(course)
            for prereqs in graph[course]:
                if not dfs(prereqs):
                    return False
            visited.remove(course)
            graph[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True