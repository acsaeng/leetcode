class Solution:
  def search(self, nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
      middle = left + ((right - left) // 2)
  
      if target == nums[middle]:
        return middle
      
      if nums[left] <= nums[middle]:
        if nums[left] <= target < nums[middle]:
          right = middle - 1
        else:
          left = middle + 1
      else:
        if nums[middle] < target <= nums[right]:
          left = middle + 1
        else:
          right = middle - 1
      
    return -1
        

print('Case 1: nums = [4, 5, 6, 7, 0, 1, 2], target = 0')
print('Answer:', Solution().search([4, 5, 6, 7, 0, 1, 2], 0))

print('\nCase 2: nums = [4, 5, 6, 7, 0, 1, 2], target = 3')
print('Answer:', Solution().search([4, 5, 6, 7, 0, 1, 2], 3))

print('\nCase 3: nums = [1], target = 0')
print('Answer:', Solution().search([1], 0))


print('\nCase: nums = [4,5,6,7,8,1,2,3], target = 8')
print('Answer:', Solution().search([4,5,6,7,8,1,2,3], 8))