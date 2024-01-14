class Solution(object):
  def rob(self, nums: list[int]) -> int:
    if len(nums) == 1:
      return nums[0]

    last_two_houses = [0, 0]

    for i in range(len(nums)):
      max_money = max(nums[i] + last_two_houses[0], last_two_houses[1])
      last_two_houses[0] = last_two_houses[1]
      last_two_houses[1] = max_money

    return max_money


print('Case 1: nums = [1, 2, 3, 1]')
print('Answer:', Solution().rob([1, 2, 3, 1]))

print('\nCase 2: nums = [2, 7, 9, 3, 1]')
print('Answer:', Solution().rob([2, 7, 9, 3, 1]))
