class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, (len(matrix) * len(matrix[0])) - 1

        while L <= R:
            M = (L + R) // 2

            row = M // len(matrix[0])
            col = M % len(matrix[0])

            if target == matrix[row][col]:
                return True
            
            elif target < matrix[row][col]:
                R = M - 1

            elif target > matrix[row][col]:
                L = M + 1

        return False