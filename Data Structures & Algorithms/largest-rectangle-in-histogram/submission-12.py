class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                idx = stack.pop()
                left = -1 if not stack else stack[-1]
                width = i - left - 1
                res = max(res, heights[idx] * width)

            stack.append(i)
        
        return res