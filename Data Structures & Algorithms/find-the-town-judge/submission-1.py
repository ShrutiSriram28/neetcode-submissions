class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0 for i in range(n + 1)]
        graph = defaultdict(lambda: [])

        for a, b in trust:
            graph[a].append(b)
            indegree[b] += 1
        
        for i in range(1, len(indegree)):
            if indegree[i] == n - 1 and i not in graph:
                return i
        
        return -1
        
        # graph = {i:[] for i in range(1, n + 1)}
        # judges = []

        # for pair in trust:
        #     graph[pair[1]].append(pair[0])
        #     if len(graph[pair[1]]) == n - 1:
        #         judges.append(pair[1])

        # for v in graph.values():
        #     for j in judges:
        #         if j in v:
        #             judges.remove(j)

        # return judges[0] if len(judges) == 1 else -1