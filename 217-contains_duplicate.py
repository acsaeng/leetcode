class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
    nums_history = set()

    for num in nums:
      if num in nums_history:
        return True
      else:
        nums_history.add(num)
    
    return False


if __name__ == '__main__':
  solution = Solution()

  print('Case 1: nums = [1, 2, 3, 1]')
  print('Answer:', solution.containsDuplicate([1, 2, 3, 1]))

  print('\nCase 2: nums = [1, 2, 3, 4]')
  print('Answer:', solution.containsDuplicate([1, 2, 3, 4]))

  print('\nCase 3: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]')
  print('Answer:', solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))