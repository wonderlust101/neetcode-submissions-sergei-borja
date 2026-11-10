class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(starts):
            seen = set(starts)
            q = deque(starts)

            while q:
                row, col = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[row][col]:
                        seen.add((nr, nc))
                        q.append((nr, nc))
            
            return seen

        pac_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atl_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        pacific, atlantic = dfs(pac_starts), dfs(atl_starts)
        return [[row, col] for row, col in pacific & atlantic]