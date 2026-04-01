class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = []
        def dfs(v, p):
            if v in visited:
                return False

            visited.append(v)
            for neighbour in graph[v]:
                if neighbour != p:
                    if not dfs(neighbour, v):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n