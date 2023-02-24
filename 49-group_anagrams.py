class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagram_groups = {}

    for str in strs:
      sorted_str = ''.join(sorted(str))
      if sorted_str in anagram_groups:
        anagram_groups[sorted_str].append(str)
      else:
        anagram_groups[sorted_str] = [str]
    
    return anagram_groups.values()


solution = Solution()

print('Case 1: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]')
print('Answer:', solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print('\nCase 2: strs = [""]')
print('Answer:', solution.groupAnagrams([""]))

print('\nCase 2: strs = ["a"]')
print('Answer:', solution.groupAnagrams(["a"]))
