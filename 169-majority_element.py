class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    count = 0

    for num in nums:
      if not count:
        candidate = num
    
      if num == candidate:
        count += 1
      else:
        count -= 1
      
    return candidate
    

print('Case 1: nums = [3, 2, 3]')
print('Answer:', Solution().majorityElement([3, 2, 3]))

print('\nCase 2: nums = [2, 2, 1, 1, 1, 2, 2]')
print('Answer:', Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))