class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        subset = []

        def dfs(i, s):
            if s == target:
                res.add(tuple(subset.copy()))
                return
            elif s > target or i == len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, s + nums[i])
            subset.pop()
            dfs(i + 1, s)
        
        dfs(0, 0)
        res = [list(i) for i in res]
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # subset = []
        # superset = []

        # def dfs(s, i):
        #     if s > target or i >= len(nums):
        #         return
        #     elif s == target:
        #         superset.append(subset.copy())
        #         return
            
        #     subset.append(nums[i])
        #     dfs(s + nums[i], i)

        #     subset.pop()
        #     dfs(s, i + 1)
        
        # dfs(0, 0)
        # return superset