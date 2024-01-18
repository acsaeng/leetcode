class Solution:
  def maxSubArray(self, nums: list[int]) -> int:
    local_max_sum = 0
    global_max_sum = nums[0]

    for num in nums:
      local_max_sum += num
      global_max_sum = max(global_max_sum, local_max_sum)

      if local_max_sum < 0:
        local_max_sum = 0
    
    return global_max_sum



print('Case 1: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]')
print('Answer:', Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

print('\nCase 2: nums = [1]')
print('Answer:', Solution().maxSubArray([1]))

print('\nCase 3: nums = [5, 4, -1, 7, 8]')
print('Answer:', Solution().maxSubArray([5, 4, -1, 7, 8]))