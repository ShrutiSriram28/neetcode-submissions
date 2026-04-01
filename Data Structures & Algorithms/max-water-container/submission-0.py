class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] >= heights[j]:
                    max_vol = max(heights[j] * abs(i - j), max_vol)
                else:
                    max_vol = max(heights[i] * abs(i - j), max_vol)

        return max_vol