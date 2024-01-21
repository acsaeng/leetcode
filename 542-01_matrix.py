class Solution:
  def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
    self.update_matrix(mat, 0, 0)
    return mat
  
  def update_matrix(self, mat, x, y):
    width, height = len(mat), len(mat[0])
    queue = []
    
    for i in range(width):
      for j in range(height):
        if mat[i][j]:
          mat[i][j] = None
        else:
          queue.append([i, j])
    
    while queue:
      x, y = queue.pop(0)

      for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        if 0 <= x + dx < width and 0 <= y + dy < height and mat[x + dx][y + dy] is None:
          mat[x + dx][y + dy] = mat[x][y] + 1
          queue.append([x + dx, y + dy])


print('Case 1: mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]')
print('Answer:', Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

print('\nCase 2: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]')
print('Answer:', Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])) 

print('\nCase : mat = [[0], [0], [0], [0], [0]]')
print('Answer:', Solution().updateMatrix([[0], [0], [0], [0], [0]]))