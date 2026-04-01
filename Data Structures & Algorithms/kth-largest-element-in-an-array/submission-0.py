class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(s, e):
            pivot, p = nums[e], s
            i = s
            while i <= e:
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
                i += 1
            p -= 1
            
            if p == len(nums) - k:
                return nums[p] 
            elif p > len(nums) - k:
                return quickselect(s, p - 1)
            else:
                return quickselect(p + 1, e)

        return quickselect(0, len(nums) - 1)