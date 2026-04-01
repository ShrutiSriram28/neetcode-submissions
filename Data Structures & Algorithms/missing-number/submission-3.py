class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor = len(nums)
        # for i in range(len(nums)):
        #     xor ^= i ^ nums[i]
        # return xor

        # return sum(range(0, len(nums) + 1)) - sum(nums)

        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res