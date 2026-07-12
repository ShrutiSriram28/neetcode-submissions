class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        
        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= len(nums):
                return 0
            
            dp[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return dp[i]
        
        return max(dfs(0), dfs(1))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # dp = [0] * (len(nums))

        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # return dp[len(nums) - 1]