class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(starts):
            seen = set(starts)
            line = deque(starts)

            while line:
                r, c = line.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]):
                        seen.add((nr, nc))
                        line.append((nr, nc))
            
            return seen

        pac_starts = [(row, 0) for row in range(rows)]  + [(0, col) for col in range(cols)]
        atl_starts = [(row, cols - 1) for row in range(rows)]  + [(rows - 1, col) for col in range(cols)]
        pacific, atlantic = dfs(pac_starts), dfs(atl_starts)
        return [[row, col] for row, col in pacific & atlantic]