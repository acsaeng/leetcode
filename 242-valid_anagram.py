class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


solution = Solution()

print('Case 1: s = "anagram", t = "nagaram"')
print('Answer:', solution.isAnagram('anagram', 'nagaram'))

print('\nCase 2: s = "rat", t = "car"')
print('Answer:', solution.isAnagram('rat', 'car'))