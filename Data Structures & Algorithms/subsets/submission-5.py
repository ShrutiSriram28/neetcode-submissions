class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        sub = []

        def dfs(i):
            if i >= len(nums) and sub not in subsets:
                subsets.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)
        
        dfs(0)
        return subsets