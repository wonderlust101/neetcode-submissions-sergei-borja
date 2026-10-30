class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(start):
            seen = set(start)
            q = deque(start)

            while q:
                row, col = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and heights[row][col] <= heights[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc))
            
            return seen

        pac_start = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atl_start = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        pacific, atlantic = dfs(pac_start), dfs(atl_start)

        return [[row,col] for row, col in pacific & atlantic]