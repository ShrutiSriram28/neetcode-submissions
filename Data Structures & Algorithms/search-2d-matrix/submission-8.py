class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        row = 0
        col = 0

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            
            elif matrix[mid][0] > target:
                bottom = mid - 1
            
            else:
                top = mid + 1

        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return False