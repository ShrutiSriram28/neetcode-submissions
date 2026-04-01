class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target and target <= matrix[i][n - 1]:
                l = 0
                r = n - 1

                while l <= r:
                    mid = (l + r)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        l += 1
                    else:
                        r -= 1
            else:
                continue

        return False