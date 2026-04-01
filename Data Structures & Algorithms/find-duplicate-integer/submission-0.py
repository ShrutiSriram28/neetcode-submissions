class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dnums = {}

        for i in nums:
            dnums[i] = dnums.get(i, 0) + 1
            if dnums[i] > 1:
                return i