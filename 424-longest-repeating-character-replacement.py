class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    left = 0
    letter_count = {}
    max_freq = 0

    for right in range(len(s)):
      letter_count[s[right]] = letter_count.get(s[right], 0) + 1
      max_freq = max(max_freq, letter_count[s[right]])
      
      if (right - left + 1) - max_freq > k:
        letter_count[s[left]] -= 1
        left += 1

    return right - left + 1


solution = Solution()

print('Case 1: s = "ABAB", k = 2')
print('Answer:', solution.characterReplacement('ABAB', 2))

print('\nCase 2: s = "AABABBA", k = 1')
print('Answer:', solution.characterReplacement('AABABBA', 1))