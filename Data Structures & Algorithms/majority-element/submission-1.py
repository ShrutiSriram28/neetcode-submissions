class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_ele = nums[0]
        max_count = 0
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > max_count:
                max_ele = n
                max_count = count[n]
        return max_ele