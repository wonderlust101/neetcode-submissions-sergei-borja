class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        line = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    line.append((row, col))

        while line:
            row, col = line.popleft()

            for dirRow, dirCol in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                newRow, newCol = row + dirRow, col + dirCol

                if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == INF:
                    grid[newRow][newCol] = grid[row][col] + 1
                    line.append((newRow, newCol))