class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            row, col = q.popleft()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    q.append((nr, nc))
                    grid[nr][nc] = grid[row][col] + 1

        