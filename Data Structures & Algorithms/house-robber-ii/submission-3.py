class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(num: List[int]) -> int:
            if len(num) == 0:
                return 0
            if len(num) == 1:
                return num[0]
            dp = [0] * (len(num))
            dp[0], dp[1] = num[0], max(num[0], num[1])

            for i in range(2, len(num)):
                dp[i] = max(dp[i - 1], dp[i - 2] + num[i])

            return dp[len(num) - 1]

        return max(helper(nums[:-1]), helper(nums[1:]))