class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # Transpose the matrix
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if i < j:
          matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reflect the matrix along the vertical
    for i in range(len(matrix)):
      for j in range(len(matrix[i]) // 2):
        matrix[i][j], matrix[i][len(matrix[i]) - 1 - j] = matrix[i][len(matrix[i]) - 1 - j], matrix[i][j]


print('Case 1: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print('Answer:', matrix)

print('\nCase 2: matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]')
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(matrix)
print('Answer:', matrix)