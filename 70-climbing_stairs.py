class Solution:
  def climbStairs(self, n: int) -> int:
    num_ways = [0, 1, 2]

    if n > 2:
      for i in range(3, n + 1):
        num_ways.append(num_ways[i - 1] + num_ways[i - 2])
      
    return num_ways[n]


if __name__ == '__main__':
  solution = Solution()

  print('Case 1: n = 2')
  print('Answer:', solution.climbStairs(2))

  print('\nCase 2: nums = 3')
  print('Answer:', solution.climbStairs(3))
