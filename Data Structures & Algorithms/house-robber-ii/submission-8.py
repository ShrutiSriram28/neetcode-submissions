class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = {}
        dp2 = {}

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def dfs(i, nums, dp):
            if i in dp:
                return dp[i]
            
            if i >= len(nums):
                return 0
            
            dp[i] = nums[i] + max(dfs(i + 2, nums, dp), dfs(i + 3, nums, dp))
            return dp[i]

        return (
            max(
                dfs(0, nums[:len(nums) - 1], dp1), 
                dfs(1, nums[:len(nums) - 1], dp1), 
                dfs(0, nums[1:], dp2), 
                dfs(1, nums[1:], dp2)
            )
        )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        
        # def helper(num: List[int]) -> int:
        #     if len(num) == 0:
        #         return 0
        #     if len(num) == 1:
        #         return num[0]
        #     dp = [0] * (len(num))
        #     dp[0], dp[1] = num[0], max(num[0], num[1])

        #     for i in range(2, len(num)):
        #         dp[i] = max(dp[i - 1], dp[i - 2] + num[i])

        #     return dp[len(num) - 1]

        # return max(helper(nums[:-1]), helper(nums[1:]))