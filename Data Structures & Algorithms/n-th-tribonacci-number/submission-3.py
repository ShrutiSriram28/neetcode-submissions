class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1

            dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            return dp[i]

        return dfs(n)
        
        # if n <= 1:
        #     return n

        # dp = [0] * (n + 1)

        # dp[0], dp[1], dp[2] = 0, 1, 1

        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        # return dp[n]