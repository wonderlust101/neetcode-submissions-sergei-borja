class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        fresh = 0
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh -= 1
                        q.append((nr, nc))
                        grid[nr][nc] = 2

            time += 1
        
        return time if not fresh else -1