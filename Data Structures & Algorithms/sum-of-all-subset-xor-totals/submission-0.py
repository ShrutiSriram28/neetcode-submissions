class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        sum_xor = 0

        def dfs(i):
            nonlocal sum_xor
            if i >= len(nums):   
                xor = 0
                for n in subset:
                    xor ^= n
                sum_xor += xor
                return 

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return sum_xor