class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sets = []

        def dfs(i, total):
            if  total == target:
                res.append(sets.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            sets.append(nums[i])
            dfs(i, total + nums[i])
            sets.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res