class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}

        for prereqs in prerequisites:
            graph[prereqs[0]].append(prereqs[1])

        visited = []
        path = []
        def dfs(course):
            print(path)
            if course in visited:
                return False
            
            if course in path:
                return True
            
            visited.append(course)
            for prereqs in graph[course]:
                if not dfs(prereqs):
                    return False
            visited.remove(course)
            path.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return path