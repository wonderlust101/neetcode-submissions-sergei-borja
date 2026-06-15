class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, (len(matrix) * len(matrix[0])) - 1

        while L <= R:
            m = (L + R) // 2

            r = m // len(matrix[0])
            c = m % len(matrix[0])

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                L = m + 1
            elif target < matrix[r][c]:
                R = m - 1
        
        return False
