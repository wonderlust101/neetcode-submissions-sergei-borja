class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            row, col = q.popleft()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
