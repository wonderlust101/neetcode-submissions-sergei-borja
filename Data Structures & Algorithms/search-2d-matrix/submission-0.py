class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) * len(matrix[0]) - 1

        while L <= R:
            mid = (L+R) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                L = mid + 1
            elif matrix[row][col] > target:
                R = mid - 1
        
        return False
