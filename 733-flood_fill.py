class Solution:
  def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    if image[sr][sc] != color:
      r, c = len(image[0]), len(image)
      old_color = image[sr][sc]
      image[sr][sc] = color

      if 0 <= sr - 1 < c and image[sr - 1][sc] == old_color:
        self.floodFill(image, sr - 1, sc, color)
      if 0 <= sr + 1 < c and image[sr + 1][sc] == old_color:
        self.floodFill(image, sr + 1, sc, color)
      if 0 <= sc - 1 < r and image[sr][sc - 1] == old_color:
        self.floodFill(image, sr, sc - 1, color)
      if 0 <= sc + 1 < r and image[sr][sc + 1] == old_color:
        self.floodFill(image, sr, sc + 1, color)
    
    return image

print('Case 1: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2')
print('Answer:', Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))

print('\nCase 2: image = [[0, 0, 0],[0, 0, 0]], sr = 0, sc = 0, color = 0')
print('Answer:', Solution().floodFill([[0, 0, 0],[0, 0, 0]], 0, 0, 0)) 