# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
  return version >= bad


class Solution:
  def firstBadVersion(self, n: int) -> int:
    left, right = 1, n

    if isBadVersion(left) == isBadVersion(right):
      return left

    while right - left > 1:
      mid = left + ((right - left) // 2)

      if isBadVersion(left) != isBadVersion(mid):
        right = mid
      else:
        left = mid
    
    return left if isBadVersion(left) else right
      

print('Case 1: n = 5, bad = 4')
bad = 4
print('Answer:', Solution().firstBadVersion(5))

print('\nCase 2: n = 1, bad = 1')
bad = 1
print('Answer:', Solution().firstBadVersion(1))
