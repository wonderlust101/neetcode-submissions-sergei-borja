class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def explore(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            area = explore(row + 1, col) + explore(row - 1, col) + explore(row, col + 1) + explore(row, col - 1)

            return area + 1

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, explore(row, col))
        
        return max_area