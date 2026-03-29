class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0

        while l < r:
            diff = r - l
            area = min(heights[l], heights[r]) * diff
            res = area if area > res else res
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res