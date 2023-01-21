import copy

class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix_copy = copy.deepcopy(matrix)

    for i, row in enumerate(matrix_copy):
      for j, num in enumerate(row):
        print('copy', matrix_copy)
        matrix[j][len(matrix_copy) - 1 - i] = num


solution = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(matrix)
print('Case 1: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]')
print('Answer:', matrix)

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solution.rotate(matrix)
print('\nCase 2: matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]')
print('Answer:', matrix)