class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) % 2:
      return False

    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
      if char in parentheses_map:
        if stack and stack[-1] == parentheses_map[char]:
          stack.pop()
        else:
          return False
      else:
        stack.append(char)

    return not stack


solution = Solution()

print('Case 1: s = "()"')
print('Answer:', solution.isValid('()'))

print('\nCase 2: s = "()[]{}"')
print('Answer:', solution.isValid('()[]{}'))

print('\nCase 3: s = "(]"')
print('Answer:', solution.isValid('(]'))