class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    stack = []
    nums_days_until_warmer_temp = [0] * len(temperatures)

    for current_day in range(len(temperatures)):
      while stack and temperatures[stack[-1]] < temperatures[current_day]:
        past_day = stack.pop()
        nums_days_until_warmer_temp[past_day] = current_day - past_day
      
      stack.append(current_day)
    
    return nums_days_until_warmer_temp


print('\nCase 1: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]')
print('Answer:', Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

print('\nCase 2: temperatures = [30, 40, 50, 60]')
print('Answer:', Solution().dailyTemperatures([30, 40, 50, 60]))

print('\nCase 3: temperatures = [30, 60, 90]')
print('Answer:', Solution().dailyTemperatures([30, 60, 90]))