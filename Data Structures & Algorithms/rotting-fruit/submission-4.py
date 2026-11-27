class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        
        time = 0
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                row, col = q.popleft()

                for nr, nc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:  
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
        
        return -1 if fresh else time