class Solution:
  def climbStairs(self, n: int) -> int:
    prev_case = 1  # Number of ways with one step
    current_case = 2  # Number of ways with two steps

    for _ in range(n - 2):
      prev_case, current_case = current_case, prev_case + current_case
      
    return current_case if n > 1 else prev_case


print('Case 1: n = 2')
print('Answer:', Solution().climbStairs(2))

print('\nCase 2: nums = 3')
print('Answer:', Solution().climbStairs(3))
