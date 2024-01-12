class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
      return False

    magazine_map = {}

    for char in magazine:
      magazine_map[char] = magazine_map.get(char, 0) + 1

    for char in ransomNote:
      if char in magazine_map and magazine_map[char] > 0:
        magazine_map[char] -= 1
      else:
        return False
    
    return True


print('Case 1: ransomNote = "a", magazine = "b"')
print('Answer:', Solution().canConstruct('a', 'b'))

print('\nCase 2: ransomNote = "aa", magazine = "ab"')
print('Answer:', Solution().canConstruct('aa', 'ab'))

print('\nCase 3: ransomNote = "aa", magazine = "aab"')
print('Answer:', Solution().canConstruct('aa', 'aab'))    