class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        top = 0
        bottom = len(matrix) - 1
        r = 0
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] == target:
                return True
            if matrix[mid - 1][-1] < target and matrix[mid][-1] > target:
                r = mid
                break
            elif matrix[mid][-1] < target:
                top = mid + 1 
            else:
                bottom = mid - 1
        print(r)
        left = 0
        right = len(matrix[r]) - 1
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        return False
            
