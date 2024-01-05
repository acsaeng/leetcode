class Solution:
  def isPalindrome(self, s: str) -> bool:
    start = 0
    end = len(s) - 1

    while start < end:
      if not s[start].isalnum():
        start += 1
      elif not s[end].isalnum():
        end -= 1
      else:
        if s[start].lower() == s[end].lower():
          start += 1
          end -= 1
        else:
          return False
    
    return True

  
solution = Solution()

print('Case 1: s = "A man, a plan, a canal: Panama"')
print('Answer:', solution.isPalindrome('A man, a plan, a canal: Panama'))

print('\nCase 2: s = "race a car"')
print('Answer:', solution.isPalindrome('race a car'))

print('\nCase 3: s = " "')
print('Answer:', solution.isPalindrome(' '))