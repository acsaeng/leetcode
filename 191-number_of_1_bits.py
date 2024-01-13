class Solution:
  def hammingWeight(self, n: int) -> int:
    num_1s = 0

    while n:
      n &= (n - 1)
      num_1s += 1
    
    return num_1s
  

print('Case 1: n = 00000000000000000000000000001011')
print('Answer:', Solution().hammingWeight(11))

print('\nCase 2: n = 00000000000000000000000010000000')
print('Answer:', Solution().hammingWeight(128))

print('\nCase 3: n = 11111111111111111111111111111101')
print('Answer:', Solution().hammingWeight(4294967293))