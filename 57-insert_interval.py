class Solution:
  def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:    
    left, right = [], []

    for interval in intervals:
      if newInterval[0] > interval[1]:
        left.append(interval)
      elif newInterval[1] < interval[0]:
        right.append(interval)
      else:
        newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
    
    return left + [newInterval] + right
      

print('Case 1: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]')
print('Answer:', Solution().insert([[1, 3], [6, 9]], [2, 5]))

print('\nCase 2: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]')
print('Answer:', Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))