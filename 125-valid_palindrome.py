class Solution:
  def isPalindrome(self, s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
      if not self.is_alphanumeric(s[left]):
        left += 1
      elif not self.is_alphanumeric(s[right]):
        right -= 1
      else:
        if s[left].lower() == s[right].lower():
          left += 1
          right -= 1
        else:
          return False
    
    return True
  
  def is_alphanumeric(self, char):
    return ord('a') <= ord(char.lower()) <= ord('z') or ord('0') <= ord(char) <= ord('9')


  
solution = Solution()

print('Case 1: s = "A man, a plan, a canal: Panama"')
print('Answer:', solution.isPalindrome('A man, a plan, a canal: Panama'))

print('\nCase 2: s = "race a car"')
print('Answer:', solution.isPalindrome('race a car'))

print('\nCase 3: s = " "')
print('Answer:', solution.isPalindrome(' '))