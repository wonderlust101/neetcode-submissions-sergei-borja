class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def scan(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0:
                return 0
            
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return (1 + scan(row + 1, col) + scan(row - 1, col) + scan(row, col + 1) + scan(row, col - 1))
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, scan(row, col))

        return maxArea
