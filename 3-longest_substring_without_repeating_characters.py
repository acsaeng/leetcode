class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()
    left = 0
    longest_substring = 0
  
    for right in range(len(s)):
      while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
      
      char_set.add(s[right])
      longest_substring = max(longest_substring, right - left + 1)
    
    return longest_substring
      

print('Case 1: s = "abcabcbb"')
print('Answer:', Solution().lengthOfLongestSubstring('abcabcbb'))

print('\nCase 2: s = "bbbbb"')
print('Answer:', Solution().lengthOfLongestSubstring('bbbbb'))

print('\nCase 3: s = "pwwkew"')
print('Answer:', Solution().lengthOfLongestSubstring('pwwkew'))