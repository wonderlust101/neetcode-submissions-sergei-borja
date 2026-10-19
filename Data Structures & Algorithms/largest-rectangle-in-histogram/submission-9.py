class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Monotonic MinStack
        best = 0

        for i, h in enumerate(heights + [0]):
            # If the top of the stack is larger than curr
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                best = max(best, heights[j] * width)

            stack.append(i)
        
        return best