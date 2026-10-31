class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def explore(starts):
            seen = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))

            return seen

        pac_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atl_starts = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]
        pacific, atlantic = explore(pac_starts), explore(atl_starts)
        return [[r, c] for r, c in pacific & atlantic]
