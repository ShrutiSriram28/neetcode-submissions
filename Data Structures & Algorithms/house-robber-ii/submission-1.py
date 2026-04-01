class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.houserobber1(nums[:len(nums) - 1]), self.houserobber1(nums[1:]))

    def houserobber1(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2