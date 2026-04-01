class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = []

        def dfs(v):
            if v not in visited:
                visited.append(v)
            for neighbour in graph[v]:
                if neighbour not in visited:
                    dfs(neighbour)

        components = 0
        for i in range(n):
            if i not in visited:
                print(i)
                dfs(i)
                components += 1

        return components