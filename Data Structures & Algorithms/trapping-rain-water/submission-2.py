class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water, max_left, max_right = 0, height[l], height[r]

        while l < r:
            if max_left < max_right:
                l += 1    
                max_left = max(max_left, height[l])
                # Finding the amount of water that can be stored over the bar l
                max_water += max_left - height[l]
            else:
                r -= 1    
                max_right = max(max_right, height[r])
                # Finding the amount of water that can be stored over the bar r
                max_water += max_right - height[r]

        return max_water
            

