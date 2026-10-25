class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def search(starts):
            seen = set(starts)
            line = deque(starts)

            while line:
                r, c = line.popleft()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        line.append((nr, nc))

            return seen
                        


        pac_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atl_starts = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]
        pacific, atlantic = search(pac_starts), search(atl_starts)
        return [(r, c) for r, c in pacific & atlantic]