class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        
        for i in nums:
            length = 0
            if i - 1 not in nums:
                while i + length in nums:
                    length += 1
                longest = max(longest, length)

        return longest
