class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    nums.sort()
    freq_map = {}
    count = 0

    for i in range(len(nums)):
      if i == 0 or nums[i] == nums[i - 1]:
        count += 1
      else:
        freq_map[count] = freq_map.get(count, []) + [nums[i - 1]]
        count = 1
    
    freq_map[count] = freq_map.get(count, []) + [nums[-1]]
    most_freq_elements = []

    while len(most_freq_elements) < k:
      most_freq_elements += freq_map[max(freq_map)]
      del freq_map[max(freq_map)]
    
    return most_freq_elements


print('Case 1: nums = [1, 1, 1, 2, 2, 3], k = 2')
print('Answer:', Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))

print('\nCase 2: nums = [1], k = 1')
print('Answer:', Solution().topKFrequent([1], 1))

print('\nCase: nums = [1, 2], k = 2')
print('Answer:', Solution().topKFrequent([1, 2], 2))