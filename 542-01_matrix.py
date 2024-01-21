class Solution:
  def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
    self.update_matrix(mat, 0, 0)
    return mat
  
  def update_matrix(self, mat, x, y):
    width, height = len(mat), len(mat[0])
    
    for x in range(width):
      for y in range(height):
        if mat[x][y]:
          left = mat[x - 1][y] if x - 1 >= 0 else float('inf')
          top = mat[x][y - 1] if y - 1 >= 0 else float('inf')
          mat[x][y] = min(left, top) + 1
    
    for x in range(width - 1, -1, -1):
      for y in range(height - 1, -1 ,-1):
        if mat[x][y]:
          right = mat[x + 1][y] if x + 1 < width else float('inf')
          bottom = mat[x][y + 1] if y + 1 < height else float('inf')
          mat[x][y] = min(mat[x][y], right + 1, bottom + 1)


print('Case 1: mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]')
print('Answer:', Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

print('\nCase 2: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]')
print('Answer:', Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])) 