class Solution:
  def longestConsecutive(self, nums: list[int]) -> int:
    nums_set = set()
    longest_seq = 0

    for num in nums:
      nums_set.add(num)

    for num in nums:
      if num - 1 not in nums_set:
        current_seq = 0
        
        while num in nums_set:
          current_seq += 1
          num += 1
      
        longest_seq = max(current_seq, longest_seq)

    return longest_seq


print('Case 1: nums = [100, 4, 200, 1, 3, 2]')
print('Answer:', Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))

print('\nCase 2: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]')
print('Answer:', Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
        