class Solution:
  def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:    
    merged_intervals = []

    for i, interval in enumerate(intervals):
      if newInterval[0] > interval[1]:
        merged_intervals.append(interval)
      elif newInterval[1] < interval[0]:
        merged_intervals.append(newInterval)
        return merged_intervals + intervals[i:]
      else:
        newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
    
    merged_intervals.append(newInterval)
    return merged_intervals
      

print('Case 1: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]')
print('Answer:', Solution().insert([[1, 3], [6, 9]], [2, 5]))

print('\nCase 2: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]')
print('Answer:', Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))