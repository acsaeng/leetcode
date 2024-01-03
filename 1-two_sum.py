class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    map = {}

    for index, num in enumerate(nums):
      diff = target - num
      
      if diff in map:
        return [map[diff], index]
      else:
        map[num] = index
    
    return


solution = Solution()

print('Case 1: nums = [2, 7, 11, 15], target = 9')
print('Answer:', solution.twoSum([2, 7, 11, 15], 9))

print('\nCase 2: nums = [3, 2, 4], target = 6')
print('Answer:', solution.twoSum([3, 2, 4], 6))

print('\nCase 3: nums = [3, 3], target = 6')
print('Answer:', solution.twoSum([3, 3], 6))