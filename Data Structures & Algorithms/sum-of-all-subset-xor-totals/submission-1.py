class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = 0
        subset = []

        def dfs(i):
            nonlocal xor
            if i >= len(nums):
                sub_xor = 0
                for i in subset:
                    sub_xor ^= i
                xor += sub_xor
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return xor