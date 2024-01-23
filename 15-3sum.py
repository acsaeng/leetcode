class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    sum_combos = []

    for i in range(len(nums)):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      
      left, right = i + 1, len(nums) - 1

      while left < right:
        sum = nums[i] + nums[left] + nums[right]

        if sum > 0:
          right -= 1
        elif sum < 0:
          left += 1
        else:
          sum_combos.append([nums[i], nums[left], nums[right]])
          left += 1

          while nums[left] == nums[left - 1] and left < right:
            left += 1

    return sum_combos


print('Case 1: nums = [-1, 0, 1, 2, -1, -4]')
print('Answer:', Solution().threeSum([-1, 0, 1, 2, -1, -4]))

print('\nCase 2: nums = [0, 1, 1]')
print('Answer:', Solution().threeSum([0, 1, 1]))

print('\nCase 3: nums = [0, 0, 0]')
print('Answer:', Solution().threeSum([0, 0, 0]))


print('\nCase: nums = [-2, 0, 0, 2, 2]')
print('Answer:', Solution().threeSum([-2, 0, 0, 2, 2]))