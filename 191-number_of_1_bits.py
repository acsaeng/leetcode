class Solution:
    def hammingWeight(self, n: int) -> int:
        n_binary = bin(n)
        return str(n_binary).count('1')


if __name__ == '__main__':
  solution = Solution()

  print('Case 1: n = 00000000000000000000000000001011')
  print('Answer:', solution.hammingWeight(11))

  print('\nCase 2: n = 00000000000000000000000010000000')
  print('Answer:', solution.hammingWeight(128))

  print('\nCase 3: n = 11111111111111111111111111111101')
  print('Answer:', solution.hammingWeight(4294967293))