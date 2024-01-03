class Solution:
  def isValid(self, s: str) -> bool:
    sequence = ''

    for char in s:
      sequence += char

      if char in [')', '}', ']']:
        if sequence[-2:] in ['()', '{}', '[]']:
          sequence = sequence[:-2]
        else:
          return False
    
    return not len(sequence)


solution = Solution()

print('Case 1: s = "()"')
print('Answer:', solution.isValid('()'))

print('\nCase 2: s = "()[]{}"')
print('Answer:', solution.isValid('()[]{}'))

print('\nCase 3: s = "(]"')
print('Answer:', solution.isValid('(]'))