class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1, 1

        for num in nums:
            tmp = curmax * num
            curmax = max(tmp, num, num * curmin)
            curmin = min(tmp, num, num * curmin)
            res = max(res, curmax)

        return res