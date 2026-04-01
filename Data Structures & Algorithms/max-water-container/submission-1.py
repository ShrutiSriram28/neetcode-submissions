class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_vol = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         if heights[i] >= heights[j]:
        #             max_vol = max(heights[j] * abs(i - j), max_vol)
        #         else:
        #             max_vol = max(heights[i] * abs(i - j), max_vol)

        # return max_vol

        max_vol = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            max_vol = max(max_vol, min(heights[l], heights[r]) * (r-l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol