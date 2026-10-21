class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        line = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    line.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        mins = 0
        while line and fresh > 0:
            for _ in range(len(line)):
                r, c = line.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        line.append((nr, nc))
            mins += 1
        
        return mins if fresh == 0 else -1