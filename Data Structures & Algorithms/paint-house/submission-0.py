class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = {}

        def dfs(i, j):
            if i >= len(costs):
                return 0

            if j < 0 or j >= len(costs[0]):
                return float("inf")
            
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = costs[i][j] + (
                    min(
                        dfs(i + 1, j - 2), 
                        dfs(i + 1, j - 1), 
                        dfs(i + 1, j + 1), 
                        dfs(i + 1, j + 2)
                    )
                )

            return dp[(i, j)]
        
        return min(dfs(0, 0), dfs(0, 1), dfs(0, 2))