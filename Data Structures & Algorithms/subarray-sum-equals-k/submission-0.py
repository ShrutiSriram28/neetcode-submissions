class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        total = 0
        res = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in prefix.keys():
                res += prefix[total - k]
            prefix[total] = prefix.get(total, 0) + 1
        
        return res
        

