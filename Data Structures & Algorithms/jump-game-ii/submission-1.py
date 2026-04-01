class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = len(nums)

        def dfs(i, jump):
            nonlocal jumps
            if i >= len(nums):
                return 
            if i == len(nums) - 1:
                jumps = min(jumps, jump)
                return
            
            for j in range(1, nums[i] + 1):
                dfs(i + j, jump + 1)

        dfs(0, 0)
        return jumps