class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        
        time = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in ((1,0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            time += 1
        
        return -1 if fresh else time