class Solution:
  def longestPalindrome(self, s: str) -> int:
    if not s: return 0
    
    letter_map = set()
    palindrome_len = 0

    for char in s:
      if char in letter_map:
        letter_map.discard(char)
        palindrome_len += 2
      else:
        letter_map.add(char)
    
    if letter_map:
      palindrome_len += 1
    
    return palindrome_len


print('Case 1: s = "abccccdd"')
print('Answer:', Solution().longestPalindrome('abccccdd'))

print('\nCase 2: s = "a"')
print('Answer:', Solution().longestPalindrome('a'))