class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        # (index, height)
        for i in range(len(heights)):
            if len(stack) == 0 or stack[-1][1] <= heights[i]:
                stack.append([i, heights[i]])
            else:
                index = 0
                while len(stack) != 0 and stack[-1][1] > heights[i]:
                    index, height = stack.pop()
                    max_area = max(max_area, (i - index) * height)
                stack.append([index, heights[i]])
        while len(stack) != 0:
            index, height = stack.pop()
            max_area = max(max_area, (len(heights) - index) * height)
        
        return max_area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []
        # max_area = 0

        # for i in range(len(heights)):
        #     if len(stack) == 0 or stack[-1][1] <= heights[i]:
        #         stack.append([i, heights[i]])
        #     else:
        #         index = 0
        #         while len(stack) != 0 and stack[-1][1] > heights[i]:
        #             index = stack[-1][0]
        #             height = stack[-1][1]
        #             max_area = max(max_area, (i - index) * height)
        #             stack.pop()
        #         stack.append([index, heights[i]])
        
        # while len(stack) != 0:
        #     i, h = stack.pop()
        #     max_area = max(max_area, (len(heights) - i) * h)

        # return max_area