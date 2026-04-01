class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        count = {}      
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                return True
        return False