class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        #     if count[n] > len(nums)//2:
        #         return n

        count = res = 0

        for n in nums:
            if count == 0:
                res = n
                count += 1
            count += (1 if n == res else -1)
        
        return res
        