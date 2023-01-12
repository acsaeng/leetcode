class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    for index1 in range(len(nums)):
      for index2 in range(len(nums)):
        if index1 != index2 and nums[index1] + nums[index2] == target:
          return [index1, index2]


if __name__ == '__main__':
  solution = Solution()

  print('Case 1: nums = [2, 7, 11, 15], target = 9')
  print('Answer:', solution.twoSum([2, 7, 11, 15], 9))

  print('\nCase 2: nums = [3, 2, 4], target = 6')
  print('Answer:', solution.twoSum([3, 2, 4], 6))

  print('\nCase 3: nums = [3, 3], target = 6')
  print('Answer:', solution.twoSum([3, 3], 6))