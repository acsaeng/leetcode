class Solution:
  def findMin(self, nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while nums[left] > nums[right]:
      middle = left + ((right - left) // 2)

      if nums[middle] > nums[right]:
        left = middle + 1
      else:
        right = middle
    
    return nums[left]


print('Case 1: nums = [3, 4, 5, 1, 2]')
print('Answer:', Solution().findMin([3, 4, 5, 1, 2]))

print('\nCase 2: nums = [4, 5, 6, 7, 0, 1, 2]')
print('Answer:', Solution().findMin([4, 5, 6, 7, 0, 1, 2]))

print('\nCase 2: nums = [11, 13, 15, 17]')
print('Answer:', Solution().findMin([11, 13, 15, 17]))