class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min_cost_spent = float("inf")

        # def dfs(i, min_cost):
        #     nonlocal min_cost_spent

        #     if i >= len(cost):
        #         min_cost_spent = min(min_cost_spent, min_cost)
        #         return min_cost_spent

        #     return min(dfs(i + 1, min_cost + cost[i]), dfs(i + 2, min_cost + cost[i]))
            
        # return min(dfs(0, 0), dfs(1, 0))
        
        dp = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in dp:
                return dp[i]

            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]

        return min(dfs(0), dfs(1))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dp = [0] * (len(cost) + 1)

        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # return dp[len(cost)]