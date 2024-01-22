from heapq import heapify, heappop

class Solution:
  def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
    for i, point in enumerate(points):
      x, y = point
      points[i] = [(x ** 2 + y ** 2) ** 0.5, x, y]

    heapify(points)
    closest_points = []

    for i in range(k):
      _, x, y = heappop(points)
      closest_points.append([x, y])
    
    return closest_points


print('Case 1: points = [[1, 3], [-2, 2]], k = 1')
print('Answer:', Solution().kClosest([[1, 3], [-2, 2]], 1))

print('\nCase 2: points = [[3, 3], [5, -1],[-2, 4]], k = 2')
print('Answer:', Solution().kClosest([[3, 3], [5, -1],[-2, 4]], 2))      