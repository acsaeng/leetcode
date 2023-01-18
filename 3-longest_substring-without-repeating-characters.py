class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    current_substring = ''
    longest_substring = ''
    s_set = set()

    for char in s:
      if char in s_set:
        if len(current_substring) > len(longest_substring):
          longest_substring = current_substring
        s_set = s_set.difference(list(current_substring.partition(char)[0]))
        current_substring = current_substring.partition(char)[2] + char
      else:
        current_substring += char
        s_set.add(char)

    if len(current_substring) > len(longest_substring):
      longest_substring = current_substring
  
    return len(longest_substring)
      

if __name__ == '__main__':
  solution = Solution()

  print('Case 1: s = "abcabcbb"')
  print('Answer:', solution.lengthOfLongestSubstring('abcabcbb'))

  print('\nCase 2: s = "bbbbb"')
  print('Answer:', solution.lengthOfLongestSubstring('bbbbb'))

  print('\nCase 3: s = "pwwkew"')
  print('Answer:', solution.lengthOfLongestSubstring('pwwkew'))