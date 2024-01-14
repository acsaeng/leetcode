class Solution:
  def addBinary(self, a: str, b: str) -> str:
    a, b = a[::-1], b[::-1]
    carry = 0
    result = ''

    for i in range(max(len(a), len(b))):
      a_digit = ord(a[i]) - ord('0') if i < len(a) else 0
      b_digit = ord(b[i]) - ord('0') if i < len(b) else 0

      total = a_digit + b_digit + carry
      result = str(total % 2) + result
      carry = total // 2

    if carry:
      result = '1' + result

    return result


print('Case 1: a = "11", b = "1"')
print('Answer:', Solution().addBinary('11', '1'))

print('\nCase 2: a = "1010", b = "1011"')
print('Answer:', Solution().addBinary('1010', '1011'))