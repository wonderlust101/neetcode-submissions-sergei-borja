class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def explore(row, col):
            if 0 > row or row >= rows or 0 > col or col >= cols or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            explore(row + 1, col)
            explore(row - 1, col)
            explore(row, col + 1)
            explore(row, col - 1)

        island = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    explore(row, col)
                    island += 1

        return island