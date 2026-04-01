class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def detectcycle(edge):
            graph = {}
            for u, v in edge:
                if u not in graph:
                    graph[u] = [v]
                else:
                    graph[u].append(v)
                if v not in graph:
                    graph[v] = [u]
                else:
                    graph[v].append(u)

            visited = []
            def dfs(v, p):
                if v in visited:
                    return True

                visited.append(v)

                for n in graph[v]:
                    if n != p:
                        if dfs(n, v):
                            return True
                return False
            
            print(graph)
            for i in graph:
                visited = []
                if dfs(i, -1):
                    return True
            return False

        for i in range(len(edges) - 1, -1, -1):
            edge = edges[:i] + edges[i + 1:]
            if not detectcycle(edge):
                return edges[i]
        return []




