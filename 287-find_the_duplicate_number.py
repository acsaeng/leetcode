class Solution:
  def findDuplicate(self, nums: list[int]) -> int:
    slow, fast = 0, 0

    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]

      if slow == fast:
        break
    
    slow2 = 0

    while True:
      slow = nums[slow]
      slow2 = nums[slow2]

      if slow == slow2:
        return slow


print('Case 1: nums = [1, 3, 4, 2, 2]')
print('Answer:', Solution().findDuplicate([1, 3, 4, 2, 2]))

print('\nCase 2: nums = [3, 1, 3, 4, 2]')
print('Answer:', Solution().findDuplicate([3, 1, 3, 4, 2]))

print('\nCase 3: nums = [3, 3, 3, 3, 3]')
print('Answer:', Solution().findDuplicate([3, 3, 3, 3, 3]))    