class Solution:
  def __init__(self):
    self.valid_combos = []
  
  def generateParenthesis(self, n: int) -> list[str]:
    self.backtrack('', n, 0, 0)
    return self.valid_combos
  
  def backtrack(self, combo, n, num_open, num_closed):
    if num_open == num_closed == n:
      self.valid_combos.append(combo)
      return
    
    if num_open < n:
      self.backtrack(combo + '(', n, num_open + 1, num_closed)
    
    if num_closed < num_open:
      self.backtrack(combo + ')', n, num_open, num_closed + 1)


print('Case 1: n = 3')
print('Answer:', Solution().generateParenthesis(3))

print('\nCase 2: n = 1')
print('Answer:', Solution().generateParenthesis(1))