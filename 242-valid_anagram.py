class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    s_map = {}
    t_map = {}

    for i in range(len(s)):
      s_map[s[i]] = s_map.get(s[i], 0) + 1
      t_map[t[i]] = t_map.get(t[i], 0) + 1

    return s_map == t_map


solution = Solution()

print('Case 1: s = "anagram", t = "nagaram"')
print('Answer:', solution.isAnagram('anagram', 'nagaram'))

print('\nCase 2: s = "rat", t = "car"')
print('Answer:', solution.isAnagram('rat', 'car'))