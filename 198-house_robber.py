class Solution(object):
  def rob(self, nums: list[int]) -> int:
    if len(nums) == 1:
      return nums[0]

    last_two_houses = [nums[0], nums[1] if nums[1] > nums[0] else nums[0]]  # Most money collected from last two houses
    max_money = max(last_two_houses)

    for i in range(2, len(nums)):
      max_money = max(nums[i] + last_two_houses[0], last_two_houses[1])
      last_two_houses[0] = last_two_houses[1]
      last_two_houses[1] = max_money

    return max_money
  

solution = Solution()

print('Case 1: nums = [1, 2, 3, 1]')
print('Answer:', solution.rob([1, 2, 3, 1]))

print('\nCase 2: nums = [2, 7, 9, 3, 1]')
print('Answer:', solution.rob([2, 7, 9, 3, 1]))
