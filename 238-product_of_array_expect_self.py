class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    left = [1] * len(nums)
    right = [1] * len(nums)

    for i in range(1, len(nums)):
      left[i] = left[i - 1] * nums[i - 1]

    for j in range(len(nums) - 2, -1, -1):
      right[j] = right[j + 1] * nums[j + 1]

    products = []

    for i in range(len(left)): 
      products.append(left[i] * right[i])

    return products
  

print('Case 1: nums = [1, 2, 3, 4]')
print('Answer:', Solution().productExceptSelf([1, 2, 3, 4]))

print('\nCase 2: [-1, 1, 0, -3, 3]')
print('Answer:', Solution().productExceptSelf([-1, 1, 0, -3, 3]))
        