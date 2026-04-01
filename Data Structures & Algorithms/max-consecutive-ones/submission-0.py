class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxc = 0
        for n in nums:
            if n == 1:
                count += 1
            elif n == 0:
                maxc = max(maxc, count)
                count = 0
        maxc = max(maxc, count)
        return maxc