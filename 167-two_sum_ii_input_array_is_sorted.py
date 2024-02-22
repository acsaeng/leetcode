class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
      current_sum = numbers[left] + numbers[right]

      if current_sum < target:
        left += 1
      elif current_sum > target:
        right -= 1
      else:
        return [left + 1, right + 1]


print('Case 1: numbers = [2, 7, 11, 15], target = 9')
print('Answer:', Solution().twoSum([2, 7, 11, 15], 9))

print('\nCase 2: numbers = [2, 3, 4], target = 6')
print('Answer:', Solution().twoSum([2, 3, 4], 6))

print('\nCase 3: numbers = [-1, 0], target = -1')
print('Answer:', Solution().twoSum([-1, 0], -1))
      