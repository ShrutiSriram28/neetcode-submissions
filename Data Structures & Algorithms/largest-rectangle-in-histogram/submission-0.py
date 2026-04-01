class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            j = i
            while stack and heights[i] < stack[-1][1]:
                max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                j = stack[-1][0]
                stack.pop()
                
            stack.append((j, heights[i]))

        # This is to calculate the max area in terms of width. 
        # The elements in the stack extend from their index to the end
        for i in range(len(stack)):
            max_area = max(max_area, stack[i][1] * (len(heights) - stack[i][0]))

        return max_area