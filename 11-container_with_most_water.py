class Solution:
  def maxArea(self, height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
      area = (right - left) * min(height[left], height[right])

      if area > max_area:
        max_area = area
      
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
    
    return max_area


print('Case 1: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]')
print('Answer:', Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

print('\nCase 2: height = [1, 1]')
print('Answer:', Solution().maxArea([1, 1]))