class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        superset = []

        def dfs(s, i):
            if s > target or i >= len(nums):
                return
            elif s == target:
                superset.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(s + nums[i], i)

            subset.pop()
            dfs(s, i + 1)
        
        dfs(0, 0)
        return superset