class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = [0] * len(height)
        maxr = [0] * len(height)
        minmaxlr = [0] * len(height)
        max_vol = 0

        for i in range(1, len(height)):
            maxl[i] = max(maxl[i-1], height[i-1])

        for i in range(len(height) - 2, -1, -1):
            maxr[i] = max(maxr[i+1], height[i+1])

        for i in range(len(height)):
            minmaxlr[i] = min(maxl[i], maxr[i]) 

        for i in range(len(height)):
            if minmaxlr[i] - height[i] < 0:
                continue
            max_vol += minmaxlr[i] - height[i]

        return max_vol