class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = float("inf")

        while l <= r:
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
            min_val = min(min_val, nums[mid])
        return min_val

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # l = 0
        # r = len(nums) - 1
        # min_val = float("inf")

        # while l <= r:
        #     mid = (l + r)//2

        #     if nums[mid] > nums[r]:
        #         l = mid + 1  
        #     else:
        #         r = mid - 1

        #     min_val = min(min_val, nums[mid])

        # return min_val