class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    s1_map = {}
    s2_map = {}
    left = right = 0

    for char in s1:
      s1_map[char] = s1_map.get(char, 0) + 1

    while right < len(s2):
      s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1

      if right - left > len(s1) - 1:
        s2_map[s2[left]] -= 1
        if s2_map[s2[left]] == 0: del s2_map[s2[left]]
        left += 1
      
      if s1_map == s2_map:
        return True

      right += 1

    return False


print('Case 1: s1 = "ab", s2 = "eidbaooo"')
print('Answer:', Solution().checkInclusion('ab', 'eidbaooo'))

print('\nCase 2: s1 = "ab", s2 = "eidboaoo"')
print('Answer:', Solution().checkInclusion('ab', 'eidboaoo'))