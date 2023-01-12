class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    map = {}

    for index, num in enumerate(nums):
      second_num = target - num
      
      if second_num in map.values():
        return [list(map.keys())[list(map.values()).index(second_num)], index]
      else:
        map[index] = num
    
    return None


if __name__ == '__main__':
  solution = Solution()

  print('Case 1: nums = [2, 7, 11, 15], target = 9')
  print('Answer:', solution.twoSum([2, 7, 11, 15], 9))

  print('\nCase 2: nums = [3, 2, 4], target = 6')
  print('Answer:', solution.twoSum([3, 2, 4], 6))

  print('\nCase 3: nums = [3, 3], target = 6')
  print('Answer:', solution.twoSum([3, 3], 6))