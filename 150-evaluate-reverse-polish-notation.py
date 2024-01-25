class Solution:
  def evalRPN(self, tokens: list[str]) -> int:
    stack = []

    for token in tokens:
      if token in ['+', '-', '*', '/']:
        second_operand = stack.pop()
        first_operand = stack.pop()

        if token == '+':
          stack.append(first_operand + second_operand)
        elif token == '-':
          stack.append(first_operand - second_operand)
        elif token == '*':
          stack.append(first_operand * second_operand)
        elif token == '/':
          stack.append(int(first_operand / second_operand))
      else:
        stack.append(int(token))

    return stack.pop()


print('Case 1: tokens = ["2", "1", "+", "3", "*"]')
print('Answer:', Solution().evalRPN(['2', '1', '+', '3', '*']))

print('\nCase 2: tokens = ["4", "13", "5", "/", "+"]')
print('Answer:', Solution().evalRPN(['4', '13', '5', '/', '+']))

print('\nCase 3: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]')
print('Answer:', Solution().evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']))