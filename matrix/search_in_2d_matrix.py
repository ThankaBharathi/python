class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix),len(matrix[0]) # row and cols size
        first , last = 0, (n*m) -1

        while first <= last:
            mid = (first + last) // 2
            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                first = mid + 1
            else:
                last = mid - 1
        return False


# brute 
for num in matrix:
    for arr in num:
        if arr == target:
            return True
return False