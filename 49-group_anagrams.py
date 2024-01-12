class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagram_groups = {}

    for str in strs:
      char_count = [0] * 26  # Represents occurances of a-z characters

      for char in str:
        char_count[ord(char) - ord('a')] += 1
      
      key = tuple(char_count)

      if key in anagram_groups:
        anagram_groups[key].append(str)
      else:
        anagram_groups[key] = [str]
    
    return anagram_groups.values()


solution = Solution()

print('Case 1: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]')
print('Answer:', solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print('\nCase 2: strs = [""]')
print('Answer:', solution.groupAnagrams([""]))

print('\nCase 2: strs = ["a"]')
print('Answer:', solution.groupAnagrams(["a"]))
