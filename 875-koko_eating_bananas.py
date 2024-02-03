import math

class Solution:
  def minEatingSpeed(self, piles: list[int], h: int) -> int:
    left, right = 1, max(piles)

    while left < right:
      middle = left + ((right - left) // 2) 
      hours = 0

      for pile in piles:
        hours += math.ceil(pile / middle)
      
      if hours <= h:
        right = middle
      else:
        left = middle + 1
      
    return left


print('Case 1: piles = [3, 6, 7, 11], h = 8')
print('Answer:', Solution().minEatingSpeed([3, 6, 7, 11], 8))

print('\nCase 2: piles = [30, 11, 23, 4, 20], h = 5')
print('Answer:', Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))

print('\nCase 3: piles = [30, 11, 23, 4, 20], h = 6')
print('Answer:', Solution().minEatingSpeed([30, 11, 23, 4, 20], 6)) 