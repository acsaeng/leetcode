class Solution:
  def search(self, nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    
    while start <= end:
      i = start + int((end - start) / 2)

      if nums[i] == target:
        return i
      elif nums[i] < target:
        start = i + 1
      else:
        end = i - 1 
    
    return -1


print('Case 1: nums = [-1, 0, 3, 5, 9, 12], target = 9')
print('Answer:', Solution().search([-1, 0, 3, 5, 9, 12], 9))

print('\nCase 2: nums = [-1, 0, 3, 5, 9, 12], target = 2')
print('Answer:', Solution().search([-1, 0, 3, 5, 9, 12], 2))