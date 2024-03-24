class Solution:
  def encode(self, strs: list[str]) -> str:
    encoded_str = ''

    for s in strs:
      encoded_str += str(len(s)) + '#' + s

    return encoded_str

  def decode(self, s: str) -> list[str]:
    decoded_str = []
    start_index = 0

    while start_index < len(s):
      end_index = start_index
      
      while s[end_index] != '#':
        end_index += 1

      str_len = int(s[start_index:end_index])

      start_index = end_index + 1
      end_index = start_index + str_len
      decoded_str.append(s[start_index:end_index])

      start_index = end_index
    
    return decoded_str


print('Case 1: ["leet", "code", "love", "you"]')
print('Answer:', Solution().decode(Solution().encode(['leet', 'code', 'love', 'you'])))

print('\nCase 2: ["we", "say", ":", "yes"]')
print('Answer:', Solution().decode(Solution().encode(['we', 'say', ':', 'yes'])))
