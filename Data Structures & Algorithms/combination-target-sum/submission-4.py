class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sub = []
        subsets = []

        def dfs(i, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                if sub not in subsets:
                    subsets.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i, total + nums[i])
            sub.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return subsets