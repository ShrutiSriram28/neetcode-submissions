class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # graph = {i:[] for i in range(n)}

        # for v1, v2 in edges:
        #     graph[v1].append(v2)
        #     graph[v2].append(v1)
        
        # visited = []

        # def dfs(v):
        #     if v not in visited:
        #         visited.append(v)
        #     for neighbour in graph[v]:
        #         if neighbour not in visited:
        #             dfs(neighbour)

        # components = 0
        # for i in range(n):
        #     if i not in visited:
        #         print(i)
        #         dfs(i)
        #         components += 1

        # return components

        graph = {i:[] for i in range(n)}
        
        for [u, v] in edges:
            # if u not in graph:
            #     graph[u] = [v]
            # elif v not in graph[u]:
                # graph[u].append(v)
            # if v not in graph:
            #     graph[v] = [u]
            # elif u not in graph[v]:
                # graph[v].append(u)
            graph[u].append(v)
            graph[v].append(u)
            
        visited = []
        stack = []
        def dfs(v):
            if v not in visited:
                stack.append(v)
                visited.append(v)
                if stack:
                    ver = stack.pop()
                    for nei in graph[ver]:
                        dfs(nei)

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components