class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = curmin = 1
        res = float("-inf")

        for n in nums:
            tmp = n * curmax
            curmax = max(tmp, n * curmin, n)
            curmin = min(tmp, n * curmin, n)
            res = max(res, curmax, curmin)
        return res