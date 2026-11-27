class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(starts):
            q = deque(starts)
            seen = set((r, c) for r, c in starts)

            while q:
                row, col = q.popleft()
                for nr, nc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr, nc) not in seen and heights[row][col] <= heights[nr][nc]:
                        seen.add((nr, nc))
                        q.append((nr, nc))
            
            return seen

        pac_starts = [(i, 0) for i in range(rows)] + [(0, i) for i in range(cols)]
        atl_starts = [[i, cols - 1] for i in range(rows)] + [[rows - 1, i] for i in range(cols)]
        pacific, atlantic = dfs(pac_starts), dfs(atl_starts)
        return [[r, c] for r, c in pacific & atlantic]