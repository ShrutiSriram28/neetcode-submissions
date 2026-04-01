class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = l + k - 1
        maxnum = []
        maxnum.append(max(nums[l:r + 1]))
        l += 1
        r += 1
        while r < len(nums):
            if nums[l - 1] != maxnum[l - 1]:
                maxnum.append(max(maxnum[l - 1], nums[r]))
            else:
                maxnum.append(max(nums[l:r + 1]))
            l += 1
            r += 1
        return maxnum