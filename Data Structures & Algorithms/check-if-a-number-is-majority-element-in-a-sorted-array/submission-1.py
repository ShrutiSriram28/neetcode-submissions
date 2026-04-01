class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        idx = len(nums)

        while l <= r:
            mid = (l + r)//2
            if nums[mid] >= target:
                r = mid - 1
                idx = mid
            else:
                l = mid + 1

        return True if (idx + len(nums)//2 < len(nums) and nums[idx + len(nums)//2] == target) else False