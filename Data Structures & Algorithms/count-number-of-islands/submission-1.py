class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def scan(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0:
                return
            
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            scan(row + 1, col)
            scan(row - 1, col)
            scan(row, col + 1)
            scan(row, col - 1)
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    scan(row, col)
                    count += 1

        return count
