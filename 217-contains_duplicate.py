class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
    num_set = set()

    for num in nums:
      if num in num_set:
        return True
      else:
        num_set.add(num)
    
    return False


solution = Solution()

print('Case 1: nums = [1, 2, 3, 1]')
print('Answer:', solution.containsDuplicate([1, 2, 3, 1]))

print('\nCase 2: nums = [1, 2, 3, 4]')
print('Answer:', solution.containsDuplicate([1, 2, 3, 4]))

print('\nCase 3: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]')
print('Answer:', solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))