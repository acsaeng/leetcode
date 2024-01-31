class Solution:
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    top, bottom = 0, len(matrix) - 1

    while top <= bottom:
      row = top + (bottom - top) // 2

      if target < matrix[row][0]:
        bottom = row - 1
      elif target > matrix[row][-1]:
        top = row + 1
      else:
        break
  
    if top > bottom:
      return False
    
    left, right = 0, len(matrix[row]) - 1

    while left <= right:
      middle = left + (right - left // 2)

      if target < matrix[row][middle]:
        right = middle - 1
      elif target > matrix[row][middle]:
        left = middle + 1
      else:
        return True
    
    return False
    

print('Case 1: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3')
print('Answer:', Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

print('\nCase 2: [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13')
print('Answer:', Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

print('\nAnswer:', Solution().searchMatrix([[1],[3]], 1))