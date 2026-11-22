class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                
                left = stack[-1] if stack else -1
                width = i - left - 1

                res = max(res, height * width)

            stack.append(i)
        
        return res