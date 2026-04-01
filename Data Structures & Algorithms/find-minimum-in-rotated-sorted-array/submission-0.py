class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = float("inf")

        while l <= r:
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                if nums[mid] < min_val:
                    min_val = nums[mid]
                l = mid + 1
                
            else:
                if nums[mid] < min_val:
                    min_val = nums[mid]
                r = mid - 1
        return min_val