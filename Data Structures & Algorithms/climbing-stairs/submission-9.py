class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i > n:
                return 0
            if i == n:
                return 1
            
            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]

        return dfs(0)









        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if n <= 2:
        #     return n
        
        # dp = [0] * (n + 1)
        # dp[1], dp[2] = 1, 2

        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]