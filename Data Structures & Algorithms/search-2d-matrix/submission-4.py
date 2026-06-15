class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        L, R = 0, (row * col) - 1

        while L <= R:
            m = (L + R) // 2

            r = m // col
            c = m % col

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                L = m + 1
            elif target < matrix[r][c]:
                R = m - 1
        
        return False
