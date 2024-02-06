class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
      return False
    
    s1_map, s2_map = {}, {}

    for i in range(len(s1)):
      s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
      s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
    
    left, right = 0, len(s1) - 1

    while right < len(s2) - 1:
      if s1_map == s2_map:
        return True
    
      s2_map[s2[left]] -= 1
      if s2_map[s2[left]] == 0: del s2_map[s2[left]]
      left += 1

      right += 1
      s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1

    return s1_map == s2_map


print('Case 1: s1 = "ab", s2 = "eidbaooo"')
print('Answer:', Solution().checkInclusion('ab', 'eidbaooo'))

print('\nCase 2: s1 = "ab", s2 = "eidboaoo"')
print('Answer:', Solution().checkInclusion('ab', 'eidboaoo'))