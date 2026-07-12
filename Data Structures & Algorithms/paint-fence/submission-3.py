class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = {}

        # if k == 1 and n > 2:
        #     return 0

        def dfs(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            if i in dp:
                return dp[i]
            
            dp[i] = (k - 1) * (dfs(i - 1) + dfs(i - 2))
            return dp[i]
        
        return dfs(n)