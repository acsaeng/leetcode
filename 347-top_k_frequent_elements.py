class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    nums_count = {}
    nums_freq = [[] for _ in range(len(nums) + 1)]

    for num in nums:
      nums_count[num] = nums_count.get(num, 0) + 1

    for num, count in nums_count.items():
      nums_freq[count].append(num)

    most_freq_elements = []

    for nums in nums_freq[::-1]:
      if len(most_freq_elements) == k:
        break
      elif nums:
        most_freq_elements += nums

    return most_freq_elements


print('Case 1: nums = [1, 1, 1, 2, 2, 3], k = 2')
print('Answer:', Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))

print('\nCase 2: nums = [1], k = 1')
print('Answer:', Solution().topKFrequent([1], 1))