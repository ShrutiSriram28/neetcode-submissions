class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}

        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])

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