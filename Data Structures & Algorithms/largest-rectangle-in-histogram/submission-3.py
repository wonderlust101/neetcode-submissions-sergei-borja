class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (i, h)
        maxArea = 0

        for i, h in enumerate(heights + [0]):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((start, h))

        
        return maxArea