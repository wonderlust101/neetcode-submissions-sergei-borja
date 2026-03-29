class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        trapped_water = [0] * len(height)

        max_height = 0
        for i in range(len(height)):
            max_left[i] = max_height
            max_height = max(max_height, height[i])

        max_height = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = max_height
            max_height = max(max_height, height[i])

        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            trapped_water[i] =  0 if water < 0 else water

        res = 0
        for i in trapped_water:
            res += i

        return res