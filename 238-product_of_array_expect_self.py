class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    products = [1] * len(nums)
    prefix, suffix = 1, 1

    for i in range(len(nums)):
      products[i] = prefix
      prefix *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
      products[i] *= suffix
      suffix *= nums[i]

    return products
  

print('Case 1: nums = [1, 2, 3, 4]')
print('Answer:', Solution().productExceptSelf([1, 2, 3, 4]))

print('\nCase 2: [-1, 1, 0, -3, 3]')
print('Answer:', Solution().productExceptSelf([-1, 1, 0, -3, 3]))
        