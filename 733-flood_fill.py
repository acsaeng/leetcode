class Solution:
  def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    queue = [[sr, sc]]
    width, height = len(image[0]), len(image)

    while queue:
      x, y = queue.pop(0)

      if 0 <= y - 1 < width and image[x][y - 1] == image[x][y] and image[x][y - 1] != color:
        queue.append([x, y - 1])
      if 0 <= y + 1 < width and image[x][y + 1] == image[x][y] and image[x][y + 1] != color:
        queue.append([x, y + 1])
      if 0 <= x - 1 < height and image[x - 1][y] == image[x][y] and image[x - 1][y] != color:
        queue.append([x - 1, y])
      if 0 <= x + 1 < height and image[x + 1][y] == image[x][y] and image[x + 1][y] != color:
        queue.append([x + 1, y])
      
      image[x][y] = color
    
    return image


print('image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2')
print('Answer:', Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))

print('\nCase 2: image = [[0, 0, 0],[0, 0, 0]], sr = 0, sc = 0, color = 0')
print('Answer:', Solution().floodFill([[0, 0, 0],[0, 0, 0]], 0, 0, 0)) 