class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = []
        for i in range(len(nums)):
            ind = []
            if target - nums[i] == nums[i]:
                if target - nums[i] in nums[i+1:]:
                    print(nums[i+1:])
                    ind.append(i) 
                    ind.append(nums[i+1:].index(target - nums[i]) + i + 1)
                    return ind

            elif target - nums[i] in nums:
                ind.append(i) 
                ind.append(nums.index(target - nums[i]))
                return ind
        return ind
            